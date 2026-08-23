#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DDLC 汉化补丁 · 翻译文本提取工具

从本地 Steam 版《Doki Doki Literature Club》游戏目录提取全部可翻译文本，
生成 Ren'Py 官方翻译骨架（tl/<语言>/*.rpy）并移动到本项目的 game/tl/ 下，
随后清除游戏目录中的全部临时痕迹（游戏目录恢复原状，不影响 Steam 完整性校验）。

用法:
    python tools/extract.py <游戏目录> [选项]

示例:
    python tools/extract.py "D:/SteamLibrary/steamapps/common/Doki Doki Literature Club"

选项:
    --lang LANG     翻译语言目录名（默认: chinese）
    --merge         增量模式：先把项目内现有翻译部署到游戏目录再提取，
                    只追加游戏中新增的文本（游戏本体更新后使用）
    --force         游戏目录存在残留 game/tl/ 时强制清除（上次提取中断的残留）
    --timeout N     等待提取进程完成的超时秒数（默认: 120）

说明:
    - 游戏目录路径只通过命令行参数传入，不写入任何项目文件，不会进入 git 记录。
    - 提取产物注释中的本地绝对路径会被自动脱敏为“文件名:行号”。
    - 全新提取会自动把项目内已有的 game/tl/<lang>/ 备份到 backups/ 目录。
    - 本工具只往游戏目录临时写入文件并在结束时删除，不修改任何原有文件。
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent

# 写入游戏 game/ 目录的开发辅助脚本名（提取结束自动删除）
HELPER_NAME = "zz_cn_extract.rpy"
DIAG_NAME = "zz_cn_extract_diag.txt"

# 嵌入的开发辅助脚本（Ren'Py/Python 2 语法）。仅在游戏以 `translate` 命令
# 启动时生效：官方 translate 命令默认跳过 .rpa 归档内的 .rpyc 脚本，此脚本
# 把归档内脚本注入提取列表，并让字符串扫描改用脚本加载阶段收集的数据。
HELPER_RPY = '''\
# cn_DDLC development-only helper: extends the `translate` command so it can
# extract translations from scripts packed inside .rpa archives (.rpyc only).
# This file is written and removed automatically by tools/extract.py.

init -50 python:
    if renpy.game.args and renpy.game.args.command == "translate":
        import os

        translator = renpy.game.script.translator

        with open(os.path.join(config.gamedir, "{{DIAG}}"), "w") as f:
            f.write("=== file_translates (dialogue blocks) ===\\n")
            for k in sorted(translator.file_translates.keys()):
                f.write("%s :: %d\\n" % (k, len(translator.file_translates[k])))

            f.write("\\n=== additional_strings (menu captions) ===\\n")
            for k in sorted(translator.additional_strings.keys()):
                f.write("%s :: %d\\n" % (k, len(translator.additional_strings[k])))

            f.write("\\n=== files inside archives ===\\n")
            for d, fn in renpy.loader.listdirfiles():
                if d is None:
                    f.write("%s\\n" % fn)

        # 对白：把翻译器已登记的全部脚本文件（含归档内文件）注入提取列表，
        # 绕过 translate_list_files() 对物理 .rpy 源文件的存在性检查。
        for fn in translator.file_translates.keys():
            if fn not in config.translate_files:
                config.translate_files.append(fn)

        # 字符串：官方扫描器只能读物理 .rpy 源码；归档内文件改用脚本加载
        # 阶段收集到的菜单文本（additional_strings）。
        import renpy.translation.scanstrings as _ss
        import renpy.translation.generation as _gen

        _orig_scan_strings = _ss.scan_strings

        def _dev_scan_strings(filename):
            if os.path.exists(filename):
                return _orig_scan_strings(filename)

            rv = [ ]
            for line, s in renpy.game.script.translator.additional_strings.get(filename, [ ]):
                rv.append(_ss.String(filename, line, s, False))
            return rv

        _ss.scan_strings = _dev_scan_strings

        def _dev_scan(min_priority=0, max_priority=299, common_only=False):
            strings = [ ]

            for filename in _gen.translate_list_files():
                strings.extend(_dev_scan_strings(os.path.normpath(filename)))

            strings.sort(key=lambda s : s.sort_key)

            rv = [ ]
            seen = set()

            for s in strings:
                if s.priority < min_priority:
                    continue
                if s.priority > max_priority:
                    continue
                if common_only and not s.common:
                    continue
                if s.text in seen:
                    continue
                seen.add(s.text)
                rv.append(s)

            return rv

        _ss.scan = _dev_scan
'''.replace("{{DIAG}}", DIAG_NAME)

BOM = b"\xef\xbb\xbf"
# 绝对路径注释（如 "# D:/xxx/yyy/game/script-ch0.rpyc:12"）
RE_ABS_COMMENT = re.compile(rb"^#\s+[A-Za-z]:[/\\].*[/\\]([^/\\]+:\d+)\s*$")
# TODO 时间戳头（"# TODO: Translation updated at ..."）
RE_TODO = re.compile(rb"^#\s*TODO: Translation updated")
# 对白翻译块（排除 "translate xxx strings:" 字符串头）
RE_BLOCK = re.compile(rb"^translate \S+ (?!strings)")
RE_OLD = re.compile(rb"^\s+old ")


def die(msg):
    print("错误: " + msg, file=sys.stderr)
    sys.exit(1)


def snapshot(root):
    """记录目录当前全部文件与子目录的相对路径集合。"""
    files, dirs = set(), set()
    for dirpath, _dirnames, filenames in os.walk(root):
        rel = os.path.normpath(os.path.relpath(dirpath, root))
        dirs.add(rel)
        for name in filenames:
            files.add(os.path.normpath(os.path.join(rel, name)))
    return files, dirs


def restore(game_dir, before_files, before_dirs):
    """删除本次运行在游戏目录新产生的文件/目录，恢复原状（只删新增，不动原有文件）。"""
    cur_files, cur_dirs = snapshot(game_dir)
    removed = 0
    for rel in sorted(cur_files - before_files):
        try:
            (game_dir / rel).unlink()
            removed += 1
        except OSError as e:
            print("  ! 无法删除 %s: %s" % (rel, e))
    # 目录从深到浅逐层删除（此时应已为空）
    for rel in sorted(cur_dirs - before_dirs, key=lambda p: p.count(os.sep), reverse=True):
        d = game_dir / rel
        if d.is_dir():
            try:
                d.rmdir()
            except OSError:
                pass
    cur_files, _ = snapshot(game_dir)
    if cur_files != before_files:
        print("  ! 游戏目录未能完全恢复（新增 %d / 缺失 %d 个文件），请人工检查"
              % (len(cur_files - before_files), len(before_files - cur_files)))
    return removed


def ddlc_process_count():
    """统计当前运行中的 DDLC.exe 进程数（tasklist CSV 输出格式与系统语言无关）。

    返回 -1 表示检测本身失败。
    """
    try:
        out = subprocess.run(["tasklist", "/NH", "/FO", "CSV"],
                             stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                             timeout=15).stdout
    except (OSError, subprocess.TimeoutExpired):
        return -1
    return sum(1 for line in out.decode("mbcs", "replace").splitlines()
               if line.startswith('"DDLC.exe"'))


def wait_engine_exit(timeout, grace=3.0):
    """等待真正的引擎进程结束。

    游戏根目录的 DDLC.exe 只是启动器：它拉起 lib/windows-i686/DDLC.exe 后立即
    退出，subprocess 只能等到启动器本身。这里轮询进程表直到引擎进程消失。
    返回是否观察到引擎进程运行。
    """
    start = time.time()
    deadline = start + timeout
    saw = False
    stable = 0
    while time.time() < deadline:
        n = ddlc_process_count()
        if n > 0:
            saw = True
            stable = 0
        else:
            stable += 1
            # 连续两次未检测到进程：引擎运行过=已结束；从未见过=启动失败，
            # 等待宽限期后交给输出校验判定
            if stable >= 2 and (saw or (time.time() - start) >= grace):
                return saw
        time.sleep(0.7)
    return saw


def sanitize_dir(tl_dir):
    """脱敏处理翻译文件：删除 TODO 时间戳行、把绝对路径注释归一化为“文件名:行号”。

    以字节方式处理，只修改纯 ASCII 的注释行，不触碰任何翻译文本。
    返回统计信息。
    """
    stats = {"files": 0, "todo": 0, "paths": 0, "blocks": 0, "strings": 0}
    for f in sorted(tl_dir.glob("*.rpy")):
        data = f.read_bytes()
        had_bom = data.startswith(BOM)
        if had_bom:
            data = data[3:]

        # 引擎在 Windows 上写出 CRLF，统一归一为 LF（避免混合行尾）
        data = data.replace(b"\r\n", b"\n")

        out = []
        for ln in data.split(b"\n"):
            if RE_TODO.match(ln):
                stats["todo"] += 1
                continue
            m = RE_ABS_COMMENT.match(ln)
            if m:
                ln = b"# " + m.group(1)
                stats["paths"] += 1
            if RE_BLOCK.match(ln):
                stats["blocks"] += 1
            if RE_OLD.match(ln):
                stats["strings"] += 1
            out.append(ln)

        # 去掉删除 TODO 头后残留的首部空行
        while out and not out[0].strip():
            out.pop(0)

        result = b"\n".join(out)
        if had_bom:
            result = BOM + result
        f.write_bytes(result)
        stats["files"] += 1
    return stats


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="DDLC 汉化补丁 · 翻译文本提取（产物进入项目 game/tl/，游戏目录自动还原）")
    parser.add_argument("game_dir", help="DDLC 游戏目录（包含 DDLC.exe 的目录）")
    parser.add_argument("--lang", default="chinese", help="翻译语言目录名（默认: chinese）")
    parser.add_argument("--merge", action="store_true",
                        help="增量模式：保留项目内已有翻译，仅追加新增文本")
    parser.add_argument("--force", action="store_true",
                        help="强制清除游戏目录残留的 game/tl/")
    parser.add_argument("--timeout", type=int, default=120,
                        help="提取进程超时秒数（默认: 120）")
    args = parser.parse_args(argv)

    if not re.fullmatch(r"[A-Za-z0-9_\-]+", args.lang):
        die("--lang 只允许字母/数字/下划线/连字符")

    game_dir = Path(args.game_dir).resolve()
    exe = game_dir / "DDLC.exe"
    game_sub = game_dir / "game"
    if not exe.is_file() or not (game_sub / "scripts.rpa").is_file():
        die("该目录不像 DDLC 游戏目录（缺少 DDLC.exe 或 game/scripts.rpa）: %s" % game_dir)

    tl_src = game_sub / "tl"
    tl_lang_src = tl_src / args.lang
    proj_tl_lang = PROJECT_DIR / "game" / "tl" / args.lang

    # 残留的 game/tl/ 会被引擎当作脚本加载，导致提取结果不完整
    if tl_src.exists():
        if not args.force:
            die("游戏目录存在残留 game/tl/（上次提取可能被中断）。确认无需保留后加 --force 重新运行")
        print("* 清除游戏目录残留 game/tl/")
        shutil.rmtree(tl_src)

    # 游戏或上次提取的引擎进程在运行会导致单实例锁冲突、提取竞态
    n = ddlc_process_count()
    if n > 0:
        die("检测到 %d 个 DDLC.exe 进程正在运行（游戏未关闭或上次提取残留），请结束进程后重试" % n)

    before_files, before_dirs = snapshot(game_dir)

    ok = False
    try:
        if args.merge:
            if not proj_tl_lang.is_dir():
                die("--merge 需要项目内已存在 game/tl/%s/" % args.lang)
            print("* 增量模式：部署项目内现有翻译到游戏目录")
            shutil.copytree(str(proj_tl_lang), str(tl_lang_src))

        print("* 写入开发辅助脚本 %s（提取结束后自动删除）" % HELPER_NAME)
        with (game_sub / HELPER_NAME).open("w", encoding="utf-8", newline="\n") as f:
            f.write(HELPER_RPY)

        print("* 运行 Ren'Py translate 命令（约 5-10 秒）...")
        cmd = [str(exe), str(game_dir), "translate", args.lang, "--no-todo"]
        try:
            # 注意：DDLC.exe 是启动器，立即返回；真正的提取在引擎子进程中进行
            proc = subprocess.run(cmd, cwd=str(PROJECT_DIR), timeout=args.timeout)
            if proc.returncode != 0:
                print("  ! 启动器返回码 %d（继续校验输出）" % proc.returncode)
        except subprocess.TimeoutExpired:
            die("提取进程超时（%d 秒），可加大 --timeout 重试" % args.timeout)

        print("* 等待引擎进程完成提取 ...")
        saw_engine = wait_engine_exit(args.timeout)
        if not saw_engine:
            print("  ! 未观察到引擎进程运行（启动可能失败），继续校验输出")

        rpy_files = sorted(tl_lang_src.glob("*.rpy")) if tl_lang_src.is_dir() else []
        if not rpy_files:
            die("提取失败：游戏目录未生成 game/tl/%s/*.rpy" % args.lang)
        print("* 提取到 %d 个翻译文件" % len(rpy_files))

        # 移动产物到项目目录；项目内已有翻译先备份
        if proj_tl_lang.exists():
            backups = PROJECT_DIR / "backups"
            backups.mkdir(exist_ok=True)
            bak = backups / ("%s-%s" % (args.lang, time.strftime("%Y%m%d-%H%M%S")))
            print("* 备份项目内现有翻译 -> %s" % bak.relative_to(PROJECT_DIR))
            shutil.move(str(proj_tl_lang), str(bak))
        proj_tl_lang.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(tl_lang_src), str(proj_tl_lang))

        stats = sanitize_dir(proj_tl_lang)
        print("* 脱敏完成: %d 个文件 / %d 个对白块 / %d 条字符串"
              "（删除 %d 行 TODO，归一化 %d 行路径注释）"
              % (stats["files"], stats["blocks"], stats["strings"],
                 stats["todo"], stats["paths"]))

        ok = True
        print("\n完成: 翻译骨架位于 %s" % proj_tl_lang.relative_to(PROJECT_DIR))
    finally:
        removed = restore(game_dir, before_files, before_dirs)
        print("* 游戏目录已还原（删除 %d 个临时文件）" % removed)

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

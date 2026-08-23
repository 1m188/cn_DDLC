# cn_DDLC —— DDLC 汉化补丁

《Doki Doki Literature Club》（Ren'Py 6.99.12.4 / Steam 版）的简体中文汉化补丁。

**原则：只新增文件、不修改游戏本体。** 补丁内容全部位于 `game/` 下的新增文件
（`tl/` 翻译、字体等），不触碰任何原有文件，因此：

- Steam「验证文件完整性」不会报差异
- 云存档、成就、Steam 覆盖层等不受影响
- 卸载补丁 = 删除新增文件

## 工具链

依赖：Python 3.8+，Windows，本地安装的 Steam 版 DDLC。

| 脚本 | 作用 |
|---|---|
| `tools/S1_extract.py` | 从游戏目录提取翻译骨架到 `game/tl/chinese/`，结束后游戏目录自动还原 |
| `tools/S2_deploy.py` | （待实现）部署补丁到游戏目录实测 |
| `tools/S3_package.py` | （待实现）打包发布 zip |

所有本地路径只通过命令行参数传入，不写入项目文件，不会进入 git 记录。

### S1 提取

```bash
python tools/S1_extract.py "D:/SteamLibrary/steamapps/common/Doki Doki Literature Club"
```

- 从 `scripts.rpa` 内的 `.rpyc` 提取全部对白与字符串，生成 Ren'Py 官方格式翻译骨架
- 产物注释中的本地绝对路径自动脱敏为 `文件名:行号`，适合开源
- 项目内已有翻译会先自动备份到 `backups/`（已 gitignore）
- 游戏本体更新后追加新文本：`--merge`；清理中断残留：`--force`

## 目录结构

```
cn_DDLC/
├── game/                  # 补丁产物（最终复制到游戏目录的内容）
│   └── tl/chinese/        # 翻译文件（对白 + 字符串）
├── tools/                 # 开发工具链（S1/S2/S3...）
├── backups/               # 自动备份（gitignore）
└── README.md
```

## 开发流程

1. **S1 提取**：生成/更新 `game/tl/chinese/` 翻译骨架
2. **翻译**：编辑 `game/tl/chinese/*.rpy`，将每块 `old`/原文对应的译文填入
   （对白块直接替换语句文本；字符串块填写 `new` 行）
3. **S2 实测**：部署到游戏目录，运行游戏逐章校对
4. **S3 打包**：产出发布 zip

## 翻译注意事项（DDLC 特有）

- 只翻译显示文本，**不得改动**任何变量名、文件名（如 `monika.chr`）、
  存档交互逻辑——DDLC 的 meta 玩法依赖这些
- 诗词小游戏词汇表（`poemwords.txt`）与 glitch 文本需要单独处理
- 文本中的 Ren'Py 标签（`{w}`、`[var]` 等）与引号转义必须保持原样

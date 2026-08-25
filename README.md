# cn_DDLC —— DDLC 汉化补丁

《Doki Doki Literature Club》（Ren'Py 6.99.12.4 / Steam 版）的简体中文汉化补丁。

**原则：只新增文件、不修改游戏本体。** 补丁内容全部位于 `game/` 下的新增文件
（`tl/` 翻译、`fonts/` 字体、`zz_cn_config.rpy` 配置），不触碰任何原有文件，因此：

- Steam「验证文件完整性」不会报差异
- 云存档、成就、Steam 覆盖层等不受影响
- 卸载补丁 = 删除新增文件

## 工具链

依赖：Python 3.8+（conda / uv / 官方安装均可），Windows，本地安装的 Steam 版 DDLC。

| 脚本 | 作用 |
|---|---|
| `tools/extract.py` | 从游戏目录提取翻译骨架到 `game/tl/chinese/`，结束后游戏目录自动还原 |

提取是低频操作——仅初次搭建、游戏本体更新、或需要补齐提取缺口时使用。
日常翻译工作直接编辑翻译文件，不依赖任何脚本。

所有涉及本地路径的参数只通过命令行传入，项目文件内不含任何机器相关路径。

### 提取

```bash
python tools/extract.py "D:/SteamLibrary/steamapps/common/Doki Doki Literature Club"
```

- 从 `scripts.rpa` 内的 `.rpyc` 提取全部对白与字符串，生成 Ren'Py 官方格式翻译骨架
- 产物注释中的本地绝对路径自动脱敏为 `文件名:行号`，行尾统一 LF，适合开源
- 项目内已有翻译会先自动备份到 `backups/`（已 gitignore）
- 游戏本体更新后追加新文本：`--merge`；清理中断残留：`--force`

## 目录结构

```
cn_DDLC/
├── game/                      # 补丁产物（玩家要复制的就是这个目录的内容）
│   ├── fonts/                 # 中文字体（思源黑体 + 霞鹜文楷，含 OFL 许可证）
│   ├── tl/chinese/            # 翻译文件（对白 + 字符串）
│   └── zz_cn_config.rpy       # 语言与字体配置（手工维护）
├── tools/extract.py           # 提取工具（低频使用）
├── backups/                   # 自动备份（gitignore）
└── README.md
```

## 开发流程

1. **提取**（一次性）：`tools/extract.py` 生成 `game/tl/chinese/` 翻译骨架
2. **翻译**（主体工作）：直接编辑 `game/tl/chinese/*.rpy` —— 对白块替换语句
   文本，字符串块填写 `new` 行
3. **测试**：把 `game/` 目录内容复制到游戏目录实测（同下述安装方式）
4. **发布**：`game/` 目录即最终产物，无需打包

### 更换字体

字体与映射配置 `game/zz_cn_config.rpy` 为手工维护：把新字体文件放入
`game/fonts/`，按文件内注释修改替换表即可。

## 安装说明（给玩家）

1. 把本项目 `game/` 目录内的**全部内容**复制到 DDLC 游戏根目录下的 `game/`
   目录中（合并，不覆盖任何原有文件）
2. 通过 Steam 正常启动游戏，界面与对白即为中文
3. 卸载：删除复制进去的 `tl/`、`fonts/`、`zz_cn_config.rpy` 及编译产生的
   `.rpyc` 即可完全还原

## 翻译注意事项（DDLC 特有）

- 只翻译显示文本，**不得改动**任何变量名、文件名（如 `monika.chr`）、
  存档交互逻辑——DDLC 的 meta 玩法依赖这些
- 诗词小游戏词汇表（`poemwords.txt`）与 glitch 文本需要单独处理
- 文本中的 Ren'Py 标签（`{w}`、`[var]` 等）与引号转义必须保持原样
- **诗歌正文不参与翻译**：诗会朗读的四首诗（含标题）存放在游戏数据
  （`Poem` 对象）中，Ren'Py 6.99 只翻译对白与字符串，无法覆盖，
  游戏内诗句仍为英文原文；仅通过 `zz_cn_config.rpy` 把诗歌手写体
  字体（m1/n1/s1/y1-3，仅含英文字形）映射为霞鹜文楷（LXGW WenKai，
  SIL OFL 1.1），以英文原文 + 中文手写观感呈现
- 界面/正文则映射为思源黑体（Noto Sans SC）

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

- 从 `scripts.rpa` 内的 `.rpyc` 提取全部对白与**可扫描字符串**（菜单标题、
  物理源文件中的 `_()` 文本），生成 Ren'Py 官方格式翻译骨架；
  **界面屏幕文本不在提取范围**（原因与应对见下文「界面文本的提取限制」）
- 产物注释中的本地绝对路径自动脱敏为 `文件名:行号`，行尾统一 LF，适合开源
- 项目内已有翻译会先自动备份到 `backups/`（已 gitignore）
- 游戏本体更新后追加新文本：`--merge`；清理中断残留：`--force`

#### 界面文本的提取限制

界面（主菜单、设置、快捷菜单、存档/读档、关于等）的按钮与提示文字存放
在 `scripts.rpa` 内的 `.rpyc` 编译产物中。引擎的翻译扫描器只能读取物理
`.rpy` 源码；对归档内的编译脚本，提取工具只能取到菜单标题——**因此 UI
屏幕文本无法自动提取，只能手工维护**在 `game/tl/chinese/screens.rpy`
（`translate chinese strings:` 块，格式与其它字符串一致）。
`tools/extract.py` 生成的骨架**永不包含** `screens.rpy`，也不会改写或
删除它。

重新提取对 `screens.rpy` 的影响：

- 增量提取（`--merge`，游戏本体更新后的常规操作）：项目翻译先部署进
  游戏目录再提取，`screens.rpy` 随整目录原样移回项目，**不会丢失**；
- 全新提取（不带 `--merge`）：项目翻译先备份到 `backups/` 再重建骨架，
  `screens.rpy` **只存在于备份中**，需要手动从 `backups/` 恢复。

手工维护 UI 翻译时注意：

- 同一字符串（`old`）只能定义一次：与 `common.rpy` 等已有条目重复时，
  Ren'Py 6.99 会报 `A translation for ... already exists` 并**闪退**
  （重复翻译是报错而非覆盖）；
- 界面文本显示时都会查翻译表（是否包裹 `_()` 不影响翻译生效），因此
  原版中未包裹 `_()` 的界面文字同样可以通过 `old`/`new` 翻译。

## 目录结构

```
cn_DDLC/
├── game/                      # 补丁产物（玩家要复制的就是这个目录的内容）
│   ├── fonts/                 # 中文字体（思源黑体 + 霞鹜文楷，含 OFL 许可证）
│   ├── tl/chinese/            # 翻译文件（对白 + 字符串；screens.rpy 为手工维护的界面文本）
│   └── zz_cn_config.rpy       # 语言与字体配置（手工维护）
├── tools/extract.py           # 提取工具（低频使用）
├── backups/                   # 自动备份（gitignore）
└── README.md
```

## 开发流程

1. **提取**（一次性）：`tools/extract.py` 生成 `game/tl/chinese/` 翻译骨架
   （对白 + 可扫描字符串；**界面文本需在骨架基础上手工补充**
   `screens.rpy`，见上文「界面文本的提取限制」）
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
- 诗词小游戏词汇表（`poemwords.txt`，228 词）经 `script-poemgame.rpy` 的
  strings 块逐词覆盖（词按钮与所有界面文本一样走字符串翻译表）；
  运行时随机生成的 glitch 词无固定原文，不覆盖
- 文本中的 Ren'Py 标签（`{w}`、`[var]` 等）与引号转义必须保持原样
- **诗歌已全部覆盖**（`game/tl/chinese/poems.rpy`）：诗的标题与正文存放在
  `Poem` 对象中，经 poem 屏幕的模板 `"[currentpoem.title]\n\n[currentpoem.text]"`
  显示；引擎显示前会对模板调用字符串翻译，因此把模板译为
  `[currentpoem.title!t]\n\n[currentpoem.text!t]`，插值时即对标题/正文
  再各查一次翻译表（`!t` 转换）。21 首诗中 19 首已译（以原作行数为骨架）；
  刻意保留原文：y23 乱码诗、n2b Base64 谜题诗、s3 的标题 "%"。
  诗歌手写体字体（m1/n1/s1/y1-3）仍经 `zz_cn_config.rpy` 映射为
  霞鹜文楷（LXGW WenKai，SIL OFL 1.1）
- 同类的「模板 + `!t`」补译还包括开篇警示语（`[splash_message]` 及其
  随机彩蛋消息，见 `splash.rpy`）
- 界面/正文则映射为思源黑体（Noto Sans SC）
- UI 界面文本（按钮/设置/存档等）手工维护于 `game/tl/chinese/screens.rpy`，
  同一 `old` 字符串全项目只能定义一次（与 `common.rpy` 等重复会启动报错，
  详见上文「界面文本的提取限制」）
- 刻意保留英文的其他内容：窗口标题栏游戏名（品牌名）、删档结局的模拟
  控制台输出、假崩溃画面（模仿引擎报错样式）、logo 等图片资源

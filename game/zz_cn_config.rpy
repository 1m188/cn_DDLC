# cn_DDLC 汉化补丁运行配置
#
# 作用：
#   1) 强制游戏语言为中文 —— 激活 game/tl/chinese/ 下的翻译
#   2) 将游戏使用的英文字体全局替换为中文字体（均 SIL OFL 1.1，可自由分发）：
#      - 界面/正文 -> 思源黑体 Noto Sans SC（许可证 OFL-NotoSansSC.txt）
#      - 角色手写体（诗歌 m1/n1/s1/y1-3）-> 龙藏体 Long Cang
#        （许可证 OFL-LongCang.txt；Google Fonts 收录的钢笔手写体；
#        仅用 Regular，加粗请求也按 Regular 渲染，以保持手写笔画风格）
#
# 维护说明：
#   - 替换表的键是游戏原字体引用（提取自 scripts.rpa 内 .rpyc 的实际常量），
#     引擎按 (字体名, bold, italic) 三元组精确匹配（renpy/text/font.py）
#   - 更换字体：把新字体文件放入 game/fonts/，修改下方变量
#     （_cn_regular / _cn_bold / _cn_hand）或对应条目的目标即可

define config.language = "chinese"

init python:
    _cn_regular = "fonts/NotoSansSC-Regular.otf"
    _cn_bold = "fonts/NotoSansSC-Bold.otf"
    _cn_hand = "fonts/LongCang-Regular.ttf"

    config.font_replacement_map.update({
        ("DejaVuSans.ttf", False, False): (_cn_regular, False, False),
        ("DejaVuSans.ttf", False, True): (_cn_regular, False, True),
        ("DejaVuSans.ttf", True, False): (_cn_bold, False, False),
        ("DejaVuSans.ttf", True, True): (_cn_bold, False, True),
        ("gui/font/Aller_Rg.ttf", False, False): (_cn_regular, False, False),
        ("gui/font/Aller_Rg.ttf", False, True): (_cn_regular, False, True),
        ("gui/font/Aller_Rg.ttf", True, False): (_cn_bold, False, False),
        ("gui/font/Aller_Rg.ttf", True, True): (_cn_bold, False, True),
        ("gui/font/F25_Bank_Printer.ttf", False, False): (_cn_regular, False, False),
        ("gui/font/F25_Bank_Printer.ttf", False, True): (_cn_regular, False, True),
        ("gui/font/F25_Bank_Printer.ttf", True, False): (_cn_bold, False, False),
        ("gui/font/F25_Bank_Printer.ttf", True, True): (_cn_bold, False, True),
        ("gui/font/Halogen.ttf", False, False): (_cn_regular, False, False),
        ("gui/font/Halogen.ttf", False, True): (_cn_regular, False, True),
        ("gui/font/Halogen.ttf", True, False): (_cn_bold, False, False),
        ("gui/font/Halogen.ttf", True, True): (_cn_bold, False, True),
        ("gui/font/RifficFree-Bold.ttf", False, False): (_cn_regular, False, False),
        ("gui/font/RifficFree-Bold.ttf", False, True): (_cn_regular, False, True),
        ("gui/font/RifficFree-Bold.ttf", True, False): (_cn_bold, False, False),
        ("gui/font/RifficFree-Bold.ttf", True, True): (_cn_bold, False, True),
        ("gui/font/VerilySerifMono.otf", False, False): (_cn_regular, False, False),
        ("gui/font/VerilySerifMono.otf", False, True): (_cn_regular, False, True),
        ("gui/font/VerilySerifMono.otf", True, False): (_cn_bold, False, False),
        ("gui/font/VerilySerifMono.otf", True, True): (_cn_bold, False, True),
        ("gui/font/m1.ttf", False, False): (_cn_hand, False, False),
        ("gui/font/m1.ttf", False, True): (_cn_hand, False, True),
        ("gui/font/m1.ttf", True, False): (_cn_hand, False, False),
        ("gui/font/m1.ttf", True, True): (_cn_hand, False, True),
        ("gui/font/n1.ttf", False, False): (_cn_hand, False, False),
        ("gui/font/n1.ttf", False, True): (_cn_hand, False, True),
        ("gui/font/n1.ttf", True, False): (_cn_hand, False, False),
        ("gui/font/n1.ttf", True, True): (_cn_hand, False, True),
        ("gui/font/s1.ttf", False, False): (_cn_hand, False, False),
        ("gui/font/s1.ttf", False, True): (_cn_hand, False, True),
        ("gui/font/s1.ttf", True, False): (_cn_hand, False, False),
        ("gui/font/s1.ttf", True, True): (_cn_hand, False, True),
        ("gui/font/y1.ttf", False, False): (_cn_hand, False, False),
        ("gui/font/y1.ttf", False, True): (_cn_hand, False, True),
        ("gui/font/y1.ttf", True, False): (_cn_hand, False, False),
        ("gui/font/y1.ttf", True, True): (_cn_hand, False, True),
        ("gui/font/y2.ttf", False, False): (_cn_hand, False, False),
        ("gui/font/y2.ttf", False, True): (_cn_hand, False, True),
        ("gui/font/y2.ttf", True, False): (_cn_hand, False, False),
        ("gui/font/y2.ttf", True, True): (_cn_hand, False, True),
        ("gui/font/y3.ttf", False, False): (_cn_hand, False, False),
        ("gui/font/y3.ttf", False, True): (_cn_hand, False, True),
        ("gui/font/y3.ttf", True, False): (_cn_hand, False, False),
        ("gui/font/y3.ttf", True, True): (_cn_hand, False, True),
    })

    # —— 断行类定制（UAX #14）——
    # 把「莫妮卡」「啊」改为 AL（字母类）：AL×AL 之间引擎只允许"间接断行"
    # （即必须隔着空格才可能断），因此由这几个字组成的连续串成为不可断词；
    # 再配合 layout "tex" 对超长单词"独占一行并允许溢出"的行为，还原
    # script-exclusives2-natsuki.rpy 中夏树台词尾音冲出对话框的效果
    # （原版该行为不可断的拉丁长词 monikammmmmm…，接收 VerilySerifMono
    # 字体 + kerning 8 的样式渲染）。
    # 副作用评估（全局，但影响极小）：
    #   - 这四个字与普通字符相邻处的断行行为不变（ID×AL、AL×ID 仍允许断行），
    #     即汉字正常的逐字断行不受影响；
    #   - 仅这四字两两相邻处不再插入断点（如「莫」「妮」「卡」相连的人名与
    #     连用的「啊」串），全游戏文本中此类组合极少位于行尾，视觉无感。
    # 详见 game/tl/chinese/script-exclusives2-natsuki.rpy 的对白块注释。
    import renpy.text.textsupport as _cn_ts

    _cn_ts.language_tailor("莫妮卡啊", "AL")

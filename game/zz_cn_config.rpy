# cn_DDLC 汉化补丁运行配置
#
# 作用：
#   1) 强制游戏语言为中文 —— 激活 game/tl/chinese/ 下的翻译
#   2) 将游戏使用的英文字体全局替换为中文字体（均 SIL OFL 1.1，可自由分发）：
#      - 界面/正文 -> 思源黑体 Noto Sans SC（许可证 OFL-NotoSansSC.txt）
#      - 角色手写体（诗歌 m1/n1/s1/y1-3）-> 霞鹜文楷 LXGW WenKai
#        （许可证 OFL-LXGWWenKai.txt；仅用 Regular，加粗请求也按
#        Regular 渲染，以保持手写笔画风格）
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
    _cn_hand = "fonts/LXGWWenKai-Regular.ttf"

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

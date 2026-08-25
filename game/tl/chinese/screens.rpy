# 界面文本翻译（screens.rpy）
# 依据 scripts.rpa 内 screens.rpyc 编译产物中的 _() 调用提取（原版字符串逐一对应）。
# 刻意保留原文的部分（未列入本文件）：
#   1. 快捷菜单中故障化显示的乱码字样（原版即为乱码，属故障效果）。
#   2. name_input 的提示语 "Please enter your name" 与损坏存档提示等未包裹 _() 的字符串。
#   3. 主菜单背景随机短语（splash.rpy init 数据，不经翻译系统）。

translate chinese strings:

    # —— 快捷菜单（quick_menu）——

    # game/screens.rpy:374
    old "Auto"
    new "自动"

    old "Skip"
    new "跳过"

    old "Save"
    new "保存"

    old "Load"
    new "读取"

    # —— 导航菜单（navigation）——

    # game/screens.rpy:435
    old "History"
    new "历史"

    old "Save Game"
    new "保存游戏"

    old "Load Game"
    new "读取游戏"

    old "Settings"
    new "设置"

    old "End Replay"
    new "结束回放"

    old "Main Menu"
    new "主菜单"

    old "Help"
    new "帮助"

    old "Quit"
    new "退出"

    # —— 游戏菜单（game_menu）——

    # game/screens.rpy:609
    old "Return"
    new "返回"

    # —— 主菜单（main_menu）——

    # game/screens.rpy:511
    old "New Game"
    new "新游戏"

    # —— 关于（about）——

    # game/screens.rpy:740
    old "About"
    new "关于"

    old "Version [config.version!t]\n"
    new "版本 [config.version!t]\n"

    old "Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"
    new "使用 {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] 制作。\n\n[renpy.license!t]"

    # —— 存档/读档（file_slots）——

    # game/screens.rpy:808
    old "{#file_time}%A, %B %d %Y, %H:%M"
    new "{#file_time}%Y年%m月%d日 %H:%M"

    old "empty slot"
    new "空存档位"

    # —— 设置（preferences）——

    # game/screens.rpy:927
    old "Display"
    new "显示"

    old "Window"
    new "窗口"

    old "Fullscreen"
    new "全屏"

    old "Rollback Side"
    new "回滚侧"

    old "Disable"
    new "禁用"

    old "Left"
    new "左"

    old "Right"
    new "右"

    old "Unseen Text"
    new "未读文本"

    old "After Choices"
    new "选择后"

    old "Text Speed"
    new "文字速度"

    old "Auto-Forward Time"
    new "自动前进时间"

    old "Music Volume"
    new "音乐音量"

    old "Sound Volume"
    new "音效音量"

    old "Voice Volume"
    new "语音音量"

    old "Test"
    new "测试"

    old "Mute All"
    new "全部静音"

    # —— 对话历史（history）——

    # game/screens.rpy:1112
    old "The dialogue history is empty."
    new "对话历史是空的。"

    # —— 名称输入（name_input）——

    # game/screens.rpy:1358
    old "OK"
    new "确定"

    # —— 确认对话框（confirm）——

    # game/screens.rpy:1429
    old "Yes"
    new "是"

    old "No"
    new "否"

    # —— 跳过指示（skip_indicator）——

    # game/screens.rpy:1498
    old "Skipping"
    new "跳过中"

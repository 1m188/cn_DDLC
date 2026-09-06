# credits.rpy 翻译（制作人员名单）
# 名单文字经 ParameterizedText 显示，同样先查字符串翻译表。
# 人名（Dan Salvato、Satchely 等）与 "Monika\n[player]" 作为署名保留原文。
# 同一 old 全项目只能定义一次（重复会导致 Ren'Py 启动报错闪退）。

translate chinese strings:

    # —— 名单头衔 ——

    old "Concept & Game Design"
    new "概念与游戏设计"
    old "Character Art"
    new "角色美术"
    old "Background Art"
    new "背景美术"
    old "Writing"
    new "剧本撰写"
    old "Music"
    new "音乐"
    old "Vocals"
    new "演唱"
    old "Special Thanks"
    new "特别鸣谢"
    old "made with love by"
    new "满怀爱意，由——"

    # —— 脚本缺失报错（dialog 屏幕）——

    old "Error: Script file is missing or corrupt.\nPlease reinstall the game."
    new "错误：脚本文件缺失或已损坏。\n请重新安装游戏。"

    # —— 片尾曲《Your Reality》歌词（ATL Text 逐行显示）——
    # 行首空格与原文保持一致；打字机分段行与整行各自成条目。

    old "The ink flows down into a dark puddle"
    new "墨水流淌成一方深色的水洼"
    old " Just move your hand -- write the way into his heart!"
    new " 只要动动手——把路写进他的心！"
    old "In my hand"
    new "在我手中"
    old " is a pen that will write a poem"
    new " 是一支能写出诗篇的笔"
    old "of me and you"
    new "写满你和我的故事"
    old "Every day,"
    new "每一天，"
    old "I imagine a future where"
    new "我想象着一个未来"
    old "I can be with you"
    new "在那里我能与你相伴"
    old "But in this world of infinite choices"
    new "但在这个有无限选择的世界里"
    old " What will it take"
    new " 要怎样才好"
    old " just to find that special day?"
    new " 才能找到那个特别的日子？"
    old "What will it take just to find that special day?"
    new "要怎样才能找到那个特别的日子？"

    # 刻意保留原文：删档结局的模拟控制台输出（"*.png deleted successfully." 等，
    # 经 "[text]" 模板插值显示，属控制台观感效果）、假崩溃画面（script-ch5 的
    # "An exception has occurred." 等，模仿引擎报错样式）。

# splash.rpy 翻译
# 对白块由提取骨架生成；strings 块含菜单文本、开篇警示语模板
# （[splash_message] → [splash_message!t]，机制见下方注释）与提示语。
# 同一 old 全项目只能定义一次（重复会导致 Ren'Py 启动报错闪退）。

# splash.rpyc:234
translate chinese splashscreen_f490803a:

    # "Deleting save data...{nw}"
    "正在删除存档数据……{nw}"

# splash.rpyc:265
translate chinese splashscreen_365de68f:

    # "This game is not suitable for children or those who are easily disturbed."
    "本游戏不适合儿童以及容易受到惊扰的玩家。"

# splash.rpyc:266
translate chinese splashscreen_b895d9b1:

    # "Individuals suffering from anxiety or depression may not have a safe experience playing this game. For content warnings, please visit: http://ddlc.moe/warning.html"
    "患有焦虑症或抑郁症的玩家，游玩本游戏时可能产生强烈不适。内容警告详见：http://ddlc.moe/warning.html"

# splash.rpyc:434
translate chinese after_load_78a4e9dc:

    # "The save file could not be loaded."
    "无法读取存档文件。"

# splash.rpyc:435
translate chinese after_load_5c5510ae:

    # "Are you trying to cheat?"
    "你是在试图作弊吗？"

# splash.rpyc:439
translate chinese after_load_46c240e4:

    # m "You're so funny."
    m "你可真逗。"

# splash.rpyc:441
translate chinese after_load_e5a463d0:

    # m "You're so funny, [persistent.playername]."
    m "你可真逗，[persistent.playername]。"

# splash.rpyc:514
translate chinese readonly_c0c137c6:

    # "The game cannot be run because you are trying to run it from a read-only location."
    "游戏无法运行，因为你正试图从只读位置启动它。"

# splash.rpyc:515
translate chinese readonly_db394637:

    # "Please copy the DDLC application to your desktop or other accessible location and try again."
    "请将 DDLC 程序复制到桌面或其他可写入的位置后再试。"

translate chinese strings:

    # splash.rpy:231
    old "A previous save file has been found. Would you like to delete your save data and start over?"
    new "检测到已有的存档数据。要删除存档并重新开始吗？"

    # splash.rpy:231
    old "Yes, delete my existing data."
    new "是，删除我现有的数据。"

    # splash.rpy:231
    old "No, continue where I left off."
    new "否，从上次的进度继续。"

    # splash.rpy:267
    old "By playing Doki Doki Literature Club, you agree that you are at least 13 years of age, and you consent to your exposure of highly disturbing content."
    new "开始游玩《心跳文学部》（Doki Doki Literature Club），即表示你已年满 13 岁，并同意接触可能引起强烈不适的内容。"

    # splash.rpy:267
    old "I agree."
    new "我同意。"

    # —— 开篇警示语（show splash_warning "[splash_message]"）——
    # 显示的是模板字符串，翻译在插值之前进行：把模板译为带 !t 的形式，
    # 使插值时再对具体消息查一次翻译表（!t 转换，renpy/substitutions.py）。

    old "[splash_message]"
    new "[splash_message!t]"

    # splash.rpy init 块：splash_message_default（一周目固定显示）
    old "This game is not suitable for children\nor those who are easily disturbed."
    new "本游戏不适合儿童，\n亦不适合容易受到惊扰的玩家。"

    # splash.rpy init 块：splash_messages（二周目起随机彩蛋消息）
    old "You are my sunshine,\nMy only sunshine"
    new "你是我的阳光，\n我唯一的阳光"
    old "I missed you."
    new "我好想你。"
    old "Play with me"
    new "陪我玩"
    old "It's just a game, mostly."
    new "这只是个游戏，大概吧。"
    old "This game is not suitable for children\nor those who are easily disturbed?"
    new "本游戏不适合儿童，\n亦不适合容易受到惊扰的玩家？"
    old "I have granted kids to hell"
    new "我已把孩子们送进了地狱"
    old "PM died for this."
    new "PM 为此而死。"
    old "It was only partially your fault."
    new "这其中只有一部分是你的错。"
    old "This game is not suitable for children\nor those who are easily dismembered."
    new "本游戏不适合儿童，\n亦不适合容易被肢解的玩家。"
    old "Don't forget to backup Monika's character file."
    new "别忘了备份莫妮卡的角色文件。"

    # 刻意保留原文（故障彩蛋）："sdfasdklfgsdfgsgoinrfoenlvbd"、"null"

    # splash.rpy 首次读档后的操作提示（dialog 屏幕）
    old "Hint: You can use the \"Skip\" button to\nfast-forward through text you've already read."
    new "提示：可以使用“跳过”按钮，\n快速略过已经读过的文本。"

    # splash.rpy 好结局文本（ATL Text，sayori_text 样式）
    old "Now everyone can be happy."
    new "现在，大家都得到幸福了。"

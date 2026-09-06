# poems.rpy 翻译（诗歌查看屏幕）
# 诗的标题与正文存放在 Poem 对象（poems.rpy init 块），经 poem 屏幕的
# 模板显示：text "[currentpoem.title]\n\n[currentpoem.text]"。
# 引擎在显示前会对该模板调用 translate_string，故把模板译为带 !t 的形式，
# 插值时再对标题/正文各查一次翻译表（!t 转换，见 renpy/substitutions.py）。
# 译制的诗以原作行数为骨架；故障体诗（y23 乱码、n2b Base64）刻意保留原文。
# 同一 old 全项目只能定义一次（重复会导致 Ren'Py 启动报错闪退）。

translate chinese strings:

    # —— poem 屏幕显示模板 ——

    old "[currentpoem.title]\n\n[currentpoem.text]"
    new "[currentpoem.title!t]\n\n[currentpoem.text!t]"

    # —— 诗的标题 ——

    # game/poems.rpy poem_y1
    old "Ghost Under the Light"
    new "灯光下的幽灵"
    # game/poems.rpy poem_y2
    old "The Raccoon"
    new "浣熊"
    # game/poems.rpy poem_y3
    old "Beach"
    new "海滩"
    # game/poems.rpy poem_y3b
    old "Ghost Under the Light pt. 2"
    new "灯光下的幽灵·其二"
    # game/poems.rpy poem_y22
    old "Wheel"
    new "轮"
    # game/poems.rpy poem_n1
    old "Eagles Can Fly"
    new "鹰能翱翔"
    # game/poems.rpy poem_n2
    old "Amy Likes Spiders"
    new "艾米喜欢蜘蛛"
    # game/poems.rpy poem_n3
    old "I'll Be Your Beach"
    new "我愿做你的海滩"
    # game/poems.rpy poem_n3b
    old "Because You"
    new "因为你"
    # game/poems.rpy poem_s1
    old "Dear Sunshine"
    new "亲爱的阳光"
    # game/poems.rpy poem_s2
    old "Bottles"
    new "瓶子"
    # game/poems.rpy poem_m1
    old "Hole in Wall"
    new "墙上的洞"
    # game/poems.rpy poem_m2
    old "Save Me"
    new "救救我"
    # game/poems.rpy poem_m3
    old "The Lady who Knows Everything"
    new "无所不知的女士"
    # game/poems.rpy poem_m4
    old "Happy End"
    new "圆满结局"

    # —— 诗的正文 ——

    # game/poems.rpy poem_y1《Ghost Under the Light》
    old "The tendrils of my hair illuminate beneath the amber glow.\nBathing.\nIt must be this one.\nThe last remaining streetlight to have withstood the test of time.\nthe last yet to be replaced by the sickening blue-green hue of the future.\nI bathe. Calm; breathing air of the present but living in the past.\nThe light flickers.\nI flicker back."
    new "发丝的卷须在琥珀色的光晕中发亮。\n沐浴着。\n一定是这一盏了。\n历经时光考验、硕果仅存的一盏街灯。\n还未被未来病态的蓝绿色调所取代的最后一盏。\n我沐浴着。平静；呼吸着此刻的空气，却活在往昔。\n灯光闪烁。\n我向它报以闪烁。"

    # game/poems.rpy poem_y2《The Raccoon》
    old "It happened in the dead of night while I was slicing bread for a guilty snack.\nMy attention was caught by the scuttering of a raccoon outside my window.\nThat was, I believe, the first time I noticed my strange tendencies as an unordinary human.\nI gave the raccoon a piece of bread, my subconscious well aware of the consequences.\nWell aware that a raccoon that is fed will always come back for more.\nThe enticing beauty of my cutting knife was the symptom.\nThe bread, my hungry curiosity.\nThe raccoon, an urge.\n\nThe moon increments its phase and reflects that much more light off of my cutting knife.\nThe very same light that glistens in the eyes of my raccoon friend.\nI slice the bread, fresh and soft. The raccoon becomes excited.\nOr perhaps I'm merely projecting my emotions onto the newly-satisfied animal.\n\nThe raccoon has taken to following me.\nYou could say that we've gotten quite used to each other.\nThe raccoon becomes hungry more and more frequently, so my bread is always handy.\nEvery time I brandish my cutting knife, the raccoon shows me its excitement.\nA rush of blood. Classic Pavlovian conditioning. I slice the bread.\nAnd I feed myself again."
    new "事情发生在万籁俱寂的深夜，我正切着面包，权当一份于心有愧的夜宵。\n窗外传来窸窣的响动，一只浣熊攫住了我的注意。\n我相信，那是我头一次察觉，自己这个异于常人的人竟有如此古怪的癖性。\n我给了浣熊一块面包，潜意识里清楚地知道后果。\n清楚地知道，一旦被喂食过，浣熊就永远会回来索要更多。\n我那把切刀诱人的美感，正是症候所在。\n面包，是我饥渴的好奇心。\n浣熊，是一股冲动。\n\n月亮渐次盈满，在我的切刀上又添几分寒光。\n同样的光，也闪现在我浣熊朋友的眼睛里。\n我切下面包，新鲜而柔软。浣熊兴奋起来。\n又或许，我只是把自己的情绪，投射到了这只刚刚餍足的小动物身上。\n\n浣熊开始跟着我了。\n可以说，我们已经相当习惯彼此。\n浣熊饿的次数越来越多，于是我的面包总是备在手边。\n每当我挥起切刀，浣熊就会向我展示它的兴奋。\n一阵血涌。教科书般的巴甫洛夫条件反射。我切下面包。\n然后，再次喂饱我自己。"

    # game/poems.rpy poem_y3《Beach》
    old "A marvel millions of years in the making.\nWhere the womb of Earth chaotically meets the surface.\nUnder a clear blue sky, an expanse of bliss--\nBut beneath gray rolling clouds, an endless enigma.\nThe easiest world to get lost in\nIs one where everything can be found.\n\nOne can only build a sand castle where the sand is wet.\nBut where the sand is wet, the tide comes.\nWill it gently lick at your foundations until you give in?\nOr will a sudden wave send you crashing down in the blink of an eye?\nEither way, the outcome is the same.\nYet we still build sand castles.\n\nI stand where the foam wraps around my ankles.\nWhere my toes squish into the sand.\nThe salty air is therapeutic.\nThe breeze is gentle, yet powerful.\nI sink my toes into the ultimate boundary line, tempted by the foamy tendrils.\nTurn back, and I abandon my peace to erode at the shore.\nDrift forward, and I return to Earth forevermore."
    new "一处历经亿万年雕琢的奇景。\n大地之子宫与地表狂乱相拥的地方。\n晴空之下，是一片无上的幸福——\n而翻卷的阴云之下，是无尽的谜。\n最容易迷失的世界\n恰是一切皆可寻得的世界。\n\n人只有在湿润的沙上，才能筑起沙堡。\n而沙湿润之处，潮水便会到来。\n它可会温柔地舔舐你的基石，直到你缴械投降？\n抑或一个骤起的浪头，眨眼间便将你击溃？\n无论哪种，结局都别无二致。\n可我们仍在筑着沙堡。\n\n我站在浪沫缠上脚踝的地方。\n脚趾陷进沙里的地方。\n咸涩的空气有疗愈之效。\n微风轻柔，却蕴藏伟力。\n我为泡沫的卷须所诱，把脚趾没入这条终极的边界线。\n转身回头，我便将安宁弃于岸畔，任其侵蚀。\n随波向前，我便永远回归大地。"

    # game/poems.rpy poem_y3b《Ghost Under the Light pt. 2》
    old "The tendrils of my hair illuminate beneath the amber glow.\nBathing.\nIn the distance, a blue-green light flickers.\nA lone figure crosses its path - a silhouette obstructing the eerie glow.\nMy heart pounds. The silhouette grows. Closer. Closer.\nI open my umbrella, casting a shadow to shield me from visibility.\nBut I am too late.\nHe steps into the streetlight. I gasp and drop my umbrella.\nThe light flickers. My heart pounds. He raises his arm.\n\nTime stops.\n\nThe only indication of movement is the amber light flickering against his outstretched arm.\nThe flickering light is in rhythm with the pounding of my heart.\nTeasing me for succumbing to this forbidden emotion.\nHave you ever heard of a ghost feeling warmth before?\nGiving up on understanding, I laugh.\nUnderstanding is overrated.\nI touch his hand. The flickering stops.\nGhosts are blue-green. My heart is amber."
    new "发丝的卷须在琥珀色的光晕中发亮。\n沐浴着。\n远处，一盏蓝绿色的灯明明灭灭。\n一道孤影横过它的光路——一个剪影，遮断了那诡异的光。\n我的心狂跳。剪影在扩大。近了。更近了。\n我撑开伞，投下一片影子，把自己藏进不可见之中。\n但我已经太迟。\n他踏进街灯的光里。我倒抽一口气，伞从手中滑落。\n灯光闪烁。心狂跳不止。他抬起手臂。\n\n时间停止了。\n\n唯一还在动的，是琥珀色的光，在他伸出的手臂上明明灭灭。\n闪烁的光，和我心跳的节拍合而为一。\n嘲弄着我向这禁忌情感的屈服。\n你可曾听说，幽灵也会感到温暖？\n我放弃理解，笑了起来。\n理解早就被高估了。\n我触碰他的手。闪烁停止了。\n幽灵是蓝绿色的。我的心是琥珀色。"

    # game/poems.rpy poem_y22《Wheel》
    old "A rotating wheel. Turning an axle. Grinding. Bolthead. Linear gearbox. Falling sky. Seven holy stakes. A docked ship. A portal to another world. A thin rope tied to a thick rope. A torn harness. Parabolic gearbox. Expanding universe. Time controlled by slipping cogwheels. Existence of God. Swimming with open water in all directions. Drowning. A prayer written in blood. A prayer written in time-devouring snakes with human eyes. A thread connecting all living human eyes. A kaleidoscope of holy stakes. Exponential gearbox. A sky of exploding stars. God disproving the existence of God. A wheel rotating in six dimensions. Forty gears and a ticking clock. A clock that ticks one second for every rotation of the planet. A clock that ticks forty times every time it ticks every second time. A bolthead of holy stakes tied to the existence of a docked ship to another world. A kaleidoscope of blood written in clocks. A time-devouring prayer connecting a sky of forty gears and open human eyes in all directions. Breathing gearbox. Breathing bolthead. Breathing ship. Breathing portal. Breathing snakes. Breathing God. Breathing blood. Breathing holy stakes. Breathing human eyes. Breathing time. Breathing prayer. Breathing sky. Breathing wheel."
    new "一只旋转的轮。转动的轴。研磨。螺栓。线性齿轮箱。坠落的天空。七根神圣的桩。一艘入坞的船。一扇通往异世界的门。细绳系着粗绳。撕裂的挽具。抛物线齿轮箱。膨胀的宇宙。被打滑的齿轮掌控的时间。上帝的存在。四面八方皆是敞开水域的游泳。溺水。用血写成的祈祷。用长着人类眼睛的食时之蛇写成的祈祷。一根连接所有活着的人类眼睛的线。神圣之桩的万花筒。指数齿轮箱。一场爆炸星辰的天空。证明上帝不存在的上帝。一只在六个维度旋转的轮。四十枚齿轮和一只滴答钟。一颗随星球每自转一周便走过一秒的钟。一颗每次滴答都要每秒滴答四十次的钟。一枚系于入坞之船通往异世界之存在的神圣之桩螺栓。一座用钟写就的血的万花筒。一道连接四十枚齿轮的天空与四方张开的人类眼睛的食时祈祷。呼吸的齿轮箱。呼吸的螺栓。呼吸的船。呼吸的门。呼吸的蛇。呼吸的上帝。呼吸的血。呼吸的神圣之桩。呼吸的人类眼睛。呼吸的时间。呼吸的祈祷。呼吸的天空。呼吸的轮。"

    # game/poems.rpy poem_n1《Eagles Can Fly》
    old "Monkeys can climb\nCrickets can leap\nHorses can race\nOwls can seek\nCheetahs can run\nEagles can fly\nPeople can try\nBut that's about it."
    new "猴子会攀爬\n蟋蟀会跳跃\n骏马会奔驰\n猫头鹰会寻觅\n猎豹会飞奔\n雄鹰会翱翔\n人们会努力\n但也就到此为止了。"

    # game/poems.rpy poem_n2《Amy Likes Spiders》
    old "You know what I heard about Amy?\nAmy likes spiders.\nIcky, wriggly, hairy, ugly spiders!\nThat's why I'm not friends with her.\n\nAmy has a cute singing voice.\nI heard her singing my favorite love song.\nEvery time she sang the chorus, my heart would pound to the rhythm of the words.\nBut she likes spiders.\nThat's why I'm not friends with her.\n\nOne time, I hurt my leg really bad.\nAmy helped me up and took me to the nurse.\nI tried not to let her touch me.\nShe likes spiders, so her hands are probably gross.\nThat's why I'm not friends with her.\n\nAmy has a lot of friends.\nI always see her talking to people.\nShe probably talks about spiders.\nWhat if her friends start to like spiders too?\nThat's why I'm not friends with her.\n\nIt doesn't matter if she has other hobbies.\nIt doesn't matter if she keeps it private.\nIt doesn't matter if it doesn't hurt anyone.\n\nIt's gross.\nShe's gross.\nThe world is better off without spider lovers.\n\nAnd I'm gonna tell everyone."
    new "你知道我听说了艾米的什么事吗？\n艾米喜欢蜘蛛。\n恶心、扭来扭去、毛茸茸、丑兮兮的蜘蛛！\n所以我才不跟她做朋友。\n\n艾米的歌声很可爱。\n我听过她唱我最喜欢的那首情歌。\n每次唱到副歌，我的心都会跟着歌词的节拍怦怦直跳。\n可她喜欢蜘蛛。\n所以我才不跟她做朋友。\n\n有一次，我的腿伤得很重。\n是艾米把我扶起来，送我去了医务室。\n我却拼命不让她碰我。\n她喜欢蜘蛛，她的手八成也恶心得很。\n所以我才不跟她做朋友。\n\n艾米有很多朋友。\n我总是看见她在跟别人讲话。\n她八成在讲蜘蛛的事。\n万一她的朋友们也开始喜欢蜘蛛怎么办？\n所以我才不跟她做朋友。\n\n就算她还有别的爱好，那也不重要。\n就算她只是私下里喜欢，那也不重要。\n就算这谁也没有伤害，那也不重要。\n\n就是恶心。\n她就是恶心。\n这个世界上没有喜欢蜘蛛的人，只会更美好。\n\n而且我要告诉所有人。"

    # game/poems.rpy poem_n3《I'll Be Your Beach》
    old "Your mind is so full of troubles and fears\nThat diminished your wonder over the years\nBut today I have a special place\nA beach for us to go.\n\nA shore reaching beyond your sight\nA sea that sparkles with brilliant light\nThe walls in your mind will melt away\nBefore the sunny glow.\n\nI'll be the beach that washes your worries away\nI'll be the beach that you daydream about each day\nI'll be the beach that makes your heart leap\nIn a way you thought had left you long ago.\n\nLet's bury your heavy thoughts in a pile of sand\nBathe in sunbeams and hold my hand\nWash your insecurities in the salty sea\nAnd let me see you shine.\n\nLet's leave your memories in a footprint trail\nSet you free in my windy sail\nAnd remember the reasons you're wonderful\nWhen you press your lips to mine.\n\nI'll be the beach that washes your worries away\nI'll be the beach that you daydream about each day\nI'll be the beach that makes your heart leap\nIn a way you thought had left you long ago.\n\nBut if you let me by your side\nYour own beach, your own escape\nYou'll learn to love yourself again."
    new "你的心里装满了烦恼与恐惧\n它们这些年一点点磨掉了你的惊奇\n而今天，我有一个特别的地方\n一片属于我们的海滩。\n\n海岸延伸到目力之外\n海面闪耀着璀璨的光\n你心头的壁垒将会消融\n在这灿烂的晴阳面前。\n\n我愿做那片海滩，把你的忧愁冲刷带走\n我愿做那片海滩，让你天天梦萦魂牵\n我愿做那片海滩，让你的心再度跳跃\n用一种你以为早已远去的方式。\n\n把沉重的思绪，埋进一座沙丘\n沐浴阳光，牵起我的手\n把心底的不安，交给咸涩的海\n让我看见你闪闪发光的模样。\n\n把回忆留在一路脚印里\n乘上我鼓满风的帆，自由来去\n记住你有多么美好\n当你的唇贴上我的唇边。\n\n我愿做那片海滩，把你的忧愁冲刷带走\n我愿做那片海滩，让你天天梦萦魂牵\n我愿做那片海滩，让你的心再度跳跃\n用一种你以为早已远去的方式。\n\n而只要你允许我陪在你身旁\n拥有你自己的海滩，你自己的港湾\n你会重新学会爱自己。"

    # game/poems.rpy poem_n3b《Because You》
    old "Tomorrow will be brighter with me around\nBut when today is dim, I can only look down.\nMy looking is a little more forward\nBecause you look at me.\n\nWhen I want to say something, I say it with a shout!\nBut my truest feelings can never come out.\nMy words are a little less empty\nBecause you listen to me.\n\nWhen something is above me, I reach for the stars.\nBut when I feel small, I don't get very far.\nMy standing is a little bit taller\nBecause you sit with me.\n\nI believe in myself with all of my heart.\nBut what do I do when it's torn all apart?\nMy faith is a little bit stronger\nBecause you trusted me.\n\nMy pen always puts my feelings to the test.\nI'm not a good writer, but my best is my best.\nMy poems are a little bit dearer\nBecause you think of me.\n\nBecause you, because you, because you."
    new "有我在，明天就会更明亮\n可今天若是阴沉，我也只能垂头丧气。\n我的目光，稍稍能望向前方了\n因为你在看着我。\n\n想说什么的时候，我会大声喊出来！\n可我最真挚的心意，却从来说不出口。\n我的话语，稍稍不那么空空荡荡了\n因为你在听我说话。\n\n有什么在我头顶之上时，我便伸手够向星辰。\n可当我自觉渺小，就怎么也够不着。\n我的站立，稍稍挺拔了一点\n因为你会坐在身边陪我。\n\n我全心全意地相信着自己。\n可当这份信念被撕成碎片，我该怎么办？\n我的信心，稍稍坚强了一点\n因为你曾经信任我。\n\n我的笔，总在考验我的心意。\n我不是什么好作者，但全力以赴便是我最好的样子。\n我的诗，稍稍珍贵了一点\n因为你在想着我。\n\n因为你，因为你，因为你。"

    # game/poems.rpy poem_n23《(无题)》
    old "I don't know how else to bring this up. But there's been something I've been worried about. Yuri has been acting kind of strange lately. You've only been here a few days, so you may not know what I mean. But she's not normally like this. She's always been quiet and polite and attentive...things like that.\n\nOkay... This is really embarrassing, but I'm forcing myself to suck it up. The truth is, I'm REALLY worried about her. But if I try talking to her, she'll just get mad at me again. I don't know what to do. I think you're the only person that she'll listen to. I don't know why. But please try to do something. Maybe you can convince her to talk to a therapist.\n\nI've always wanted to try being better friends with Yuri, and it really hurts me to see this happening. I know I'm going to hate myself later for admitting that, but right now I don't care. I just feel so helpless. So please see if you can do something to help. I don't want anything bad to happen to her. I'll make you cupcakes if I have to. Just please try to do something.\n\nAs for Monika... I don't know why, but she's been really dismissive about this. It's like she just wants us to ignore it. So I'm mad at her right now, and that's why I'm coming to you about this. DON'T LET HER KNOW I WROTE THIS!!!! Just pretend like I gave you a really good poem, okay? I'm counting on you. Thanks for reading."
    new "我不知道还能怎么开口。但有件事一直让我很担心。优里最近的样子有点怪。你才来了几天，可能不明白我在说什么。可她平时不是这样的。她一直是安安静静、彬彬有礼、体贴入微的……就是这样的人。\n\n好……说这个真的很丢脸，但我是在逼自己硬着头皮说。事实上，我真的非常非常担心她。可我要是去找她谈，她只会再对我发火。我不知道该怎么办。我觉得，她唯一听得进话的人就是你。我也不知道为什么。但请你想想办法吧。也许你能劝她去找心理医生聊聊。\n\n我一直很想和优里变成更好的朋友，看到这一切发生，我真的很难受。我知道事后我一定会为说出这句话而讨厌自己，但现在我顾不上了。我只是觉得太无助了。所以求你看看能不能帮她做点什么。我不希望她出任何事。实在不行，我可以给你烤纸杯蛋糕。求你了，想想办法吧。\n\n至于莫妮卡……我不知道为什么，她对此特别不当回事，就好像只想让我们别去管一样。所以我现在很生她的气，这才来找你说这些。千万别让她知道我写了这个！！！！你就假装我给了你一首特别棒的诗，好吗？全靠你了。谢谢你读到这里。"

    # game/poems.rpy poem_s1《Dear Sunshine》
    old "The way you glow through my blinds in the morning\nIt makes me feel like you missed me.\nKissing my forehead to help me out of bed.\nMaking me rub the sleepy from my eyes.\n\nAre you asking me to come out and play?\nAre you trusting me to wish away a rainy day?\nI look above. The sky is blue.\nIt's a secret, but I trust you too.\n\nIf it wasn't for you, I could sleep forever.\nBut I'm not mad.\n\nI want breakfast."
    new "清晨你透过百叶窗洒进来的光\n让我觉得，你是想我了。\n亲吻我的额头，哄我起床。\n催我揉掉眼睛里的瞌睡。\n\n你是在叫我出去玩吗？\n你是相信我能许愿赶走雨天吗？\n我抬头看看。天空蓝蓝的。\n这是个秘密，不过我也信任你哦。\n\n要不是有你，我能一直睡到永远。\n但我才不会生气。\n\n我要吃早饭。"

    # game/poems.rpy poem_s2《Bottles》
    old "I pop off my scalp like the lid of a cookie jar.\nIt's the secret place where I keep all my dreams.\nLittle balls of sunshine, all rubbing together like a bundle of kittens.\nI reach inside with my thumb and forefinger and pluck one out.\nIt's warm and tingly.\nBut there's no time to waste! I put it in a bottle to keep it safe.\nAnd I put the bottle on the shelf with all of the other bottles.\nHappy thoughts, happy thoughts, happy thoughts in bottles, all in a row.\n\nMy collection makes me lots of friends.\nEach bottle a starlight to make amends.\nSometimes my friend feels a certain way.\nDown comes a bottle to save the day.\n\nNight after night, more dreams.\nFriend after friend, more bottles.\nDeeper and deeper my fingers go.\nLike exploring a dark cave, discovering the secrets hiding in the nooks and crannies.\nDigging and digging.\nScraping and scraping.\n\nI blow dust off my bottle caps.\nIt doesn't feel like time elapsed.\nMy empty shelf could use some more.\nMy friends look through my locked front door.\n\nFinally, all done. I open up, and in come my friends.\nIn they come, in such a hurry. Do they want my bottles that much?\nI frantically pull them from the shelf, one after the other.\nHolding them out to each and every friend.\nEach and every bottle.\nBut every time I let one go, it shatters against the tile between my feet.\nHappy thoughts, happy thoughts, happy thoughts in shards, all over the floor.\n\nThey were supposed to be for my friends, my friends who aren't smiling.\nThey're all shouting, pleading. Something.\nBut all I hear is echo, echo, echo, echo, echo\nInside my head."
    new "我掀开头盖，就像拧开饼干罐的盖子。\n那是我珍藏所有梦的秘密地方。\n一颗颗小太阳，像一窝小猫似的挤挤挨挨。\n我把拇指和食指伸进去，捏出一颗来。\n暖暖的，麻酥酥的。\n可没时间磨蹭啦！我把它装进瓶子，好好保管。\n再把瓶子放上架子，和其他的瓶子摆在一起。\n快乐的念头，快乐的念头，装进瓶子的快乐的念头，排成一排排。\n\n我的收藏给我带来了好多朋友。\n每只瓶子都是一点星光，用来赔礼和好。\n有时我的朋友心情不好。\n就取下一只瓶子，赶来救场。\n\n一夜又一夜，更多的梦。\n一个朋友又一个朋友，更多的瓶子。\n我的手指越伸越深。\n像在探索一座黑暗的洞穴，发现藏在角角落落里的秘密。\n挖呀，挖呀。\n抠呀，抠呀。\n\n我吹掉瓶盖上的灰。\n感觉不出时间过去了多久。\n我空空的架子还可以再放一些。\n我的朋友们，从我上了锁的前门望进来。\n\n终于，全都弄好了。我打开门，朋友们涌了进来。\n他们急匆匆地挤进来。有那么想要我的瓶子吗？\n我手忙脚乱地从架子上拿，一只接一只。\n递给每一个朋友。\n每一只瓶子。\n可每当我松手放开一只，它就在我脚边的瓷砖上摔得粉碎。\n快乐的念头，快乐的念头，摔成碎片的快乐的念头，铺了一地。\n\n它们本来是要给我的朋友们的，那些笑不出来的朋友们。\n他们都在喊，都在求。喊着什么。\n可我听见的只有回声，回声，回声，回声，回声\n在我脑子里。"

    # game/poems.rpy poem_s3《%》
    old "Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of\nGet.\nOut.\nOf.\nMy.\nHead.\n\n\n\nGet out of my head before I do what I know is best for you.\nGet out of my head before I listen to everything she said to me.\nGet out of my head before I show you how much I love you.\nGet out of my head before I finish writing this poem.\n\n\n\n\n\n\n\nBut a poem is never actually finished.\nIt just stops moving."
    new "离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离开我的脑海。离。\n开。\n我。\n的。\n脑。\n海。\n\n\n\n在我做出那件我知道对你最好的事之前，离开我的脑海。\n在我把她说过的一切照单全收之前，离开我的脑海。\n在我让你看见我有多爱你之前，离开我的脑海。\n在我写完这首诗之前，离开我的脑海。\n\n\n\n\n\n\n\n但一首诗其实永远不会写完。\n它只是停止了移动。"

    # game/poems.rpy poem_m1《Hole in Wall》
    old "It couldn't have been me.\nSee, the direction the spackle protrudes.\nA noisy neighbor? An angry boyfriend? I'll never know. I wasn't home.\nI peer inside for a clue.\nNo! I can't see. I reel, blind, like a film left out in the sun.\nBut it's too late. My retinas.\nAlready scorched with a permanent copy of the meaningless image.\nIt's just a little hole. It wasn't too bright.\nIt was too deep.\nStretching forever into everything.\nA hole of infinite choices.\nI realize now, that I wasn't looking in.\nI was looking out.\nAnd he, on the other side, was looking in."
    new "那不可能是我。\n你看，墙灰鼓出来的方向。\n吵闹的邻居？愤怒的男友？我永远无从知晓。当时我不在家。\n我凑近洞口想找点线索。\n不！什么也看不见。我踉跄后退，双目失明，像一卷被忘在太阳底下的胶片。\n但已经太迟。我的视网膜。\n早已被烙上那张无意义的图像，永远的拷贝。\n只是一个小小的洞而已。并没有太亮。\n只是太深了。\n向着万物，无限延伸。\n一个盛满无限选择的洞。\n我现在才明白，当时我并不是在往里看。\n我是在往外看。\n而他，在另一侧，正往里看。"

    # game/poems.rpy poem_m21《Hole in Wall》
    old "But he wasn't looking at me.\nConfused, I frantically glance at my surroundings.\nBut my burned eyes can no longer see color.\nAre there others in this room? Are they talking?\nOr are they simply poems on flat sheets of paper,\nThe sound of frantic scrawling playing tricks on my ears?\nThe room begins to crinkle.\nClosing in on me.\nThe air I breathe dissipates before it reaches my lungs.\nI panic. There must be a way out.\nIt's right there. He's right there.\n\nSwallowing my fears, I brandish my pen."
    new "可他看的并不是我。\n我慌乱地环顾四周，一头雾水。\n但我被灼伤的眼睛，再也看不见颜色。\n这房间里还有别人吗？他们在说话吗？\n又或者他们只是平铺的纸上的一首首诗，\n那疯狂涂写的沙沙声，不过是我耳边的错觉？\n房间开始起皱。\n向我挤压过来。\n我呼吸的空气，还没到肺里就消散了。\n我慌了。一定有出口的。\n就在那里。他就在那里。\n\n我咽下恐惧，挥起手中的笔。"

    # game/poems.rpy poem_m2《Save Me》
    old "The colors, they won't stop.\nBright, beautiful colors\nFlashing, expanding, piercing\nRed, green, blue\nAn endless\ncacophony\nOf meaningless\nnoise\n\n\nThe noise, it won't stop.\nViolent, grating waveforms\nSqueaking, screeching, piercing\nSine, cosine, tangent\n    Like playing a chalkboard on a turntable\n        Like playing a vinyl on a pizza crust\nAn endless\npoem\nOf meaningless\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoad Me\n    "
    new "那些颜色，它们不肯停。\n明亮的、美丽的颜色\n闪烁着、扩张着、刺穿着\n红、绿、蓝\n一场无尽的\n嘈杂喧闹\n全都是毫无意义的\n杂音\n\n\n那杂音，它不肯停。\n狂暴的、刺耳的波形\n吱嘎作响、尖啸刺耳、穿透一切\n正弦、余弦、正切\n    像在唱机的转盘上播放一块黑板\n        像在披萨饼皮上播放一张黑胶\n一首无尽的\n诗\n全都是毫无意义的\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n读取我\n    "

    # game/poems.rpy poem_m22《Save Me》
    old "The colors, they won't\nBright, bea t ful c l rs\nFlash ng, exp nd ng, piercing\nRed, green, blue\nAn  ndless\nCACOPHONY\nOf meaningless\nnoise\n\n\nThe noise, it won't STOP.\nViol nt, grating w vef rms\nSq e king, screech ng, piercing\nSINE, COSINE, TANGENT\n    Like play ng a ch lkboard on a t rntable\n        Like playing a KNIFE on a BREATHING RIBCAGE\n n  ndl ss\np  m\nOf m  n ngl ss\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDelete Her\n    "
    new "那些颜色，它们不会\n明亮的、美丽的 色 彩\n闪 烁、扩 张、刺穿\n红、绿、蓝\n无 尽的\n嘈 杂 喧 闹\n全都是毫无意义的\n杂音\n\n\n那杂音，它不会停止。\n狂 暴的、刺耳的波 形\n吱 嘎作响、尖啸刺 耳、穿透一切\n正 弦、余 弦、正 切\n    像在 转 盘上播放一 块黑板\n        像用一 把刀在 呼吸的肋骨 上演奏\n 无 尽的\n诗\n毫无意 义\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n删除她\n    "

    # game/poems.rpy poem_m3《The Lady who Knows Everything》
    old "An old tale tells of a lady who wanders Earth.\nThe Lady who Knows Everything.\nA beautiful lady who has found every answer,\nAll meaning,\nAll purpose,\nAnd all that was ever sought.\n\nAnd here I am,\n\n\n              a feather\n\n\nLost adrift the sky, victim of the currents of the wind.\n\nDay after day, I search.\nI search with little hope, knowing legends don't exist.\nBut when all else has failed me,\nWhen all others have turned away,\nThe legend is all that remains - the last dim star glimmering in the twilit sky.\n\nUntil one day, the wind ceases to blow.\nI fall.\nAnd I fall and fall, and fall even more.\nGentle as a feather.\nA dry quill, expressionless.\n\nBut a hand catches me between the thumb and forefinger.\nThe hand of a beautiful lady.\nI look at her eyes and find no end to her gaze.\n\nThe Lady who Knows Everything knows what I am thinking.\nBefore I can speak, she responds in a hollow voice.\n\"I have found every answer, all of which amount to nothing.\nThere is no meaning.\nThere is no purpose.\nAnd we seek only the impossible.\nI am not your legend.\nYour legend does not exist.\"\n\nAnd with a breath, she blows me back afloat, and I pick up a gust of wind."
    new "一则古老的传说，讲一位游荡人间的女士。\n无所不知的女士。\n一位美丽的女士，她已寻得所有的答案，\n所有的意义，\n所有的目的，\n以及一切曾被追寻之物。\n\n而我在这里，\n\n\n              一根羽毛\n\n\n随风漂泊天际，沦为气流的猎物。\n\n日复一日，我寻找着。\n我怀着渺茫的希望寻找，明知传说并不存在。\n可当一切的一切都令我失望，\n当所有其他人都转身离去，\n传说便是仅剩的——暮色天空中最后一颗黯淡闪烁的星。\n\n直到有一天，风停了。\n我坠落。\n我落啊落，落啊落，落得更深更远。\n轻柔得像一根羽毛。\n一支干涸的笔，毫无表情。\n\n可一只手用拇指和食指接住了我。\n一位美丽女士的手。\n我望进她的眼睛，却望不见她凝视的尽头。\n\n无所不知的女士知道我在想什么。\n我还没来得及开口，她便用空洞的声音答道：\n“我已寻得所有的答案，而它们加起来一文不值。\n没有意义。\n没有目的。\n我们追寻的只是不可能。\n我不是你的传说。\n你的传说并不存在。”\n\n随着一口气息，她把我重新吹上天空，而我乘上了一阵风。"

    # game/poems.rpy poem_m4《Happy End》
    old "Pen in hand, I find my strength.\nThe courage endowed upon me by my one and only love.\nTogether, let us dismantle this crumbling world\nAnd write a novel of our own fantasies.\n\nWith a flick of her pen, the lost finds her way.\nIn a world of infinite choices, behold this special day.\n\nAfter all,\nNot all good times must come to an end."
    new "笔在手中，我找到了我的力量。\n那份由我唯一的爱所赋予我的勇气。\n来吧，让我们一起拆解这分崩离析的世界\n书写一部属于我们两人幻想的小说。\n\n她笔尖轻挥，迷失的人便找到了归途。\n在无限选择的世界里，请见证这个特别的日子。\n\n毕竟，\n并非所有美好的时光，都注定要有终点。"

    # 刻意保留原文：mdpnfbo,jrfp（标题与正文均为刻意乱码）；T3BlbiBZb3VyIFRoaXJkIEV5ZQ==（标题与正文均为 Base64 谜题）

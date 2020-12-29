from django.shortcuts import render


def emoticon(request):
    return render(request, 'emoticon/emoticon.html', {
                'classicos': classicos_ascii,
                'feliz': feliz,
                'triste': triste,
                'nervoso': nervoso,
                'surpresa': surpresa,
                'saudacao': saudacao,
                'fofos': fofos
                })

classicos_ascii = [
    ';)',
    '^_~',
    ';-)',
    ':)',
    '^_^',
    '^_____^',
    ':-)',
    ':D',
    '^0^',
    ':-D',
    ':P',
    ':-P',
    ';P',
    ':(',
    ':-(',
    'U_U',
    ':[',
    '>:(',
    '>"<',
    '):',
    ':-O',
    'O.O',
    'OwO',
    ':-()',
    '~_~',
    '^o^',
    ':-S',
    '<3',
    '^3^',
    ':-x',
    ':/',
    'X_X',
    '=/',
    ';(',
    'T_T',
    ';[',
    '+_+',
    'O_O',
    ':O',
    '¬_¬',
    ';_;',
    '=.=',
    ';]',
    '^_+',
    ';O)',
    ':-]',
    '^.^',
    '=)',
    ':O)',
    ':-3',
    '=D',
    ':|',
    '-.-',
    '>_<',
    ':O(',
    '*_*',
    '=[',
    '8-)',
    '^^;',
    ':-*',
    'B-)',
    '=_=',
    '-0-',
    ':S',
    '$_$',
    ':-$',
    '>.<',
    '-_-',
    '>',
    '<',
    ':]',
    '^^',
    '=]',
    ';D',
    '^_-',
    '=P',
    ':(',
    'Y.Y',
    '=(',
    ]

feliz = [
    '*^_^*',
    'o(*^＠^*)o',
    '(∩_∩)',
    '`(*>﹏<*)′',
    '(*^▽^*)',
    '（*＾-＾*）',
    '(*^_^*)',
    '(❁´◡`❁)',
    '(⌒ω⌒)',
    '(p≧w≦q)',
    '(≧▽≦)',
    '≧°◡°≦',
    '(＾皿＾)っ',
    '\^o^/',
    '(‾◡‾)',
    '╰(*°▽°*)╯',
    'o(*^▽^*)┛',
    'o(*￣▽￣*)ブ',
    '(^∇^*)',
    'o(*￣︶￣*)o',
    '(*^‿^*)',
    'ヽ(o^  ^o)ﾉ',
    '($_$)',
    '(☆▽☆)',
    '(＠⌒ー⌒)ノ',
    'o(*ﾟ▽ﾟ*)o',
    '♪(´▽｀)',
    '(', '*^-^)ρ',
    '(^0^*', ')',
    '(^v^)',
    '(^///^)',
    "\(◦'⌣'◦)/",
    '(o^▽^o)',
    '(*⌒―⌒*)',
    '(✯◡✯)',
    '(◕‿◕)',
    '(⁀ᗢ⁀)',
    '(⌒▽⌒)',
    '(˙▿˙)',
    '(¯▿¯)',
    '\(^ヮ^)/',
    '(＾▽＾)',
    '(＠＾◡＾)',
    '(｡•́‿•̀｡)',
    '(*￣▽￣)b'
    ]

triste = [
    '＞﹏＜',
    '＞︿＜',
    '<(＿　＿)>',
    '(>_<)',
    '.·´¯`(>▂<)´¯`·.',
    '(┬┬﹏┬┬)',
    '≧ ﹏ ≦',
    '〒▽〒',
    '(T_T)',
    '(˘_˘٥)',
    '(≧﹏ ≦)',
    '(TヘT)',
    '~~>_<~~',
    '(T﹏T)',
    'X﹏X',
    'ಥ_ಥ',
    '(~_~;)',
    '(⌣́_⌣̀)',
    '(⌣̩̩́_⌣̩̩̀)',
    '(҂⌣̀_⌣́)',
    '(._.)',
    '(｡•́︿•̀｡)'
    '(╥﹏╥)',
    '(⌣́_⌣̀)\(˘⌣˘ )',
    '(ノ_<。)',
    '(-_-)',
    '(´-ω-`)',
    '(μ_μ)',
    '( ;ω; )',
    '(｡╯︵╰｡)',
    '(>д<)',
    '〒﹏〒',
    '(っ˘̩╭╮˘̩)っ',
    '（π_π）' 
    ]

nervoso = [
    '╰（‵□′）╯',
    '(╬▔皿▔)╯',
    '（︶^︶）',
    '╚(•⌂•)╝',
    '┗|｀O′|┛',
    '(TロT)σ',
    '<( ‵□′)>',
    '<( ‵□′)───C＜─___-)',
    '(҂⌣̀_⌣́)',
    '(ﾉ °益°)ﾉ',
    '( o｀ω′)ノ',
    '(╯▔皿▔)╯',
    '(σ｀д′)σ',
    '(►__◄)',
    'ᕦ(ò_óˇ)ᕤ',
    '(`Д´)',
    '(ㆆ_ㆆ)',
    'ಠ_ಠ┌',
    '( ಠ_ಠ)┘',
    'ಠ╭╮ಠ',
    '눈_눈',
    '(¬_¬")',
    '( •̀ .̫ •́ )',
    '۹( ÒہÓ )۶',
    '(`･︿´･ )',
    '(; ⌣̀_⌣́)',
    '(＃`Д´)',
    '( ` ω ´ )',
    '(`ー´)',
    '凸(`△´＃)',
    '(` ﾛ ´)'       
    ]

surpresa = [
    'w(°ｏ°)w',
    '(⊙ｏ⊙)',
    'ヽ(°〇°)ﾉ',
    'Σ(O_O)',
    '(⊙_⊙;)',
    'Σ(°ロ°)',
    '(⊙_⊙)',
    '(o_O)',
    '(O_O;)',
    '(O.O)',
    'Σ(□_□)',
    '∑(O_O;)',
    '(°ロ°)!',
    '(＠_＠;)',
    '(o_O)!',
    '(□_□)',
    '(>•o•)>' 
    ]

saudacao = [
    'ヾ(•ω•`)o',
    '\(￣︶￣*\))',
    '(* ￣3)(ε￣ *)',
    '(*￣3￣)',
    '╭( ´･･)ﾉ(._.`)',
    '(｡･∀･)ﾉﾞ',
    '(ToT)/~~~',
    '(∪.∪ ).zZ!',
    '(￣o￣).zZ',
    '(づ￣ 3￣)づ',
    '❤～\(@^0^@)/',
    'ヾ(^▽^*)',
    'v(￣o￣).zZ',
    '(^_-)db(-_^)',
    '(>‿◠)',
    'ヽ(*￣▽￣*)ノ',
    '(＾Ｕ＾)ノ~ＹＯ',
    'ヾ(￣▽￣)Bye~Bye~',
    '( ﾟдﾟ)つ Bye',
    'd=====(￣▽￣*)b',
    'ｄ(╹ڡ╹ )ノ',
    '(^^ゞ',
    '~\(≧▽≦)/~',
    'b(￣▽￣)d',
    '(☞ﾟヮﾟ)☞☜(ﾟヮﾟ☜)'
    ]

fofos = [
    '(✿◡‿◡)',
    '(=^ ◡ ^=)',
    '(=^･ω･^=)',
    'V●ᴥ●V',
    '(･ω<)☆',
    '(づ◡﹏◡)づ',
    '(* ^ ω ^)',
    '(´｡• ω •｡`)',
    '(o･ω･o)',
    '(´• ω •`)',
    '(.❛ ᴗ ❛.)',
    '(=∩ω∩=)',
    '(⁄ ⁄•⁄ω⁄•⁄ ⁄)',
    '(・3・)',
    '(„• ֊ •„)',
    '(°ε° )',
    '(๑˃ᴗ˂)ﻭ',
    '(˃ᆺ˂)',
    "(-'_'-)",
    'ฅ^•ﻌ•^ฅ'
    ]

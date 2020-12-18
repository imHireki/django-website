from django.shortcuts import render


def emoji(request):
    christmas = [
        u'\U0001F476', u'\U0001F47C', u'\U0001F514', u'\U0001F385',
        u'\U0001F936', u'\U0001F46A', u'\U0001F98C', u'\U0001F36A',
        u'\U0001F95B', u'\U0001F377', u'\U0001F31F', u'\U0001F525',
        u'\U0001F384', u'\U0001F381', u'\U0001F9E6', u'\U0001F56F',
        u'\U0001F6D0',
        u'\u26EA',  u'\u2603', u'\u26C4', u'\u2744', u'\u271D',
        '🧑‍🎄', 
    ]

    faces = [
        u'\U0001f600', u'\U0001f601', u'\U0001f602', u'\U0001f603',
        u'\U0001f604', u'\U0001f605', u'\U0001f606', u'\U0001f923', 
        u'\U0001f60A', u'\U0001f607', u'\U0001f972', u'\U0001f642',
        u'\u263A'
    ]
    
    return render(request, 'emoji/emoji.html',{'christmas': christmas, 'faces': faces})

from django.shortcuts import render


def emoticon(request):
    # Page Render
    if request.path == '/en/emoticon':
        nav = {'nav_emoji': '/en/emoji', 'nav_convert': '/en/convert-case',
            'nav_emoticon': '/en/emoticon'}
        return render(request, 'emoticon/en_emoticon.html',
                      {'nav': nav, 'foo': 'foo'})
    elif request.path == '/pt/emoticon':
        nav = {'nav_emoji': '/pt/emoji', 'nav_convert': '/pt/convert-case',
            'nav_emoticon': '/pt/emoticon'}
        return render(request, 'emoticon/pt_emoticon.html',
                      {'nav': nav, 'foo': 'foo'})

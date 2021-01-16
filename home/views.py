from django.shortcuts import render


def home(request):
    links = {
    'nav_emoji': '/en/emoji',
    'nav_convert': '/en/convert-case',
    'nav_emoticon': '/en/emoticon'
    }
    transl = {
        'name_c': 'CONVERT CASE',
        'dev': 'Developed with \U0001F499 by Hireki'
        }
    return render(request, 'home/home.html', {
        'links': links, 'transl': transl})
    

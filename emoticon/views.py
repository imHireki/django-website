from django.shortcuts import render


def emoticon(request):
    html_lang = {
        'hreflang0': '<link rel="alternate" hreflang="en" href="https://www.shadesapps.com/en/emoticon" />',
        'hreflang1': '<link rel="alternate" hreflang="pt" href="https://www.shadesapps.com/pt/emoticon" />',
        'hreflang2': '<link rel="alternate" hreflang="x-default" href="https://www.shadesapps.com/en/emoticon" />'
        }
    # Page Render
    if request.path == '/en/emoticon':
        links = {
            'nav_emoji': '/en/emoji',
            'nav_convert': '/en/convert-case',
            'nav_emoticon': '/en/emoticon'}
        transl = {
            'name_c': 'CONVERT CASE',
            'dev': 'Developed with \U0001F499 by Hireki',
            'desc': 'You will find here lists with emoticons, kaomojis, Japanese emoticons and ASCII Japanese emojis, happy, sad, anger, shrug and cute emojis, for copy and paste.'
            }
        return render(request, 'emoticon/en_emoticon.html', {
            'links': links, 'transl': transl, 'html_lang': html_lang})
        
    elif request.path == '/pt/emoticon':
        links = {
            'nav_emoji': '/pt/emoji',
            'nav_convert': '/pt/convert-case',
            'nav_emoticon': '/pt/emoticon'
            }
        transl = {
            'name_c': 'LETRAS DIFERENTES',
            'dev':'Desenvolvido com \U0001F499 por Hireki',
            'desc': 'Encontre aqui listas de reações kaomoji, emojis e emoticons Japoneses em ASCII, feliz, triste, com raiva, e fofos, além de Lenny Face e outros.'
            }
        return render(request, 'emoticon/pt_emoticon.html', {
            'links': links, 'transl': transl, 'html_lang': html_lang})

from django.shortcuts import render


def text_emoji(request):
    return render(request, 'textemoji/textEmoji.html')

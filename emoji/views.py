from django.shortcuts import render


def emoji(request):
    return render(request, 'emoji/emoji.html')

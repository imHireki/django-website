from django.shortcuts import render


def emoticon(request):
    return render(request, 'emoticon/emoticon.html')

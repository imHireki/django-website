from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')


def letras_diferentes(request):
    return render(request, 'pages/letrasDiferentes.html')

from django.shortcuts import render
from pages.forms import InputForms


def home(request):
    return render(request, 'pages/home.html')


def letras_diferentes(request):

    form = InputForms(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        form.a = form.cleaned_data['origin']

    return render(request, 'pages/letrasDiferentes.html', context)

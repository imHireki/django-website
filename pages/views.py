from django.shortcuts import render
from django.http import HttpResponse
from pages.forms import InputForms
from django.utils.html import format_html



def home(request):
    return render(request, 'pages/home.html')


def letras_diferentes(request):
    # Form 
    form = InputForms(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        form.d = form.cleaned_data['origin']

    # Buttons
    if(request.POST.get('submit')):
        if (request.POST.get('submit')) == 'btn-a':
            form.d = format_html('&#120094')
            return render(request, 'pages/letrasDiferentes.html', context)


    return render(request, 'pages/letrasDiferentes.html', context)

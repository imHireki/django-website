from django.shortcuts import render, redirect
from django.views.generic.base import View
from convert.forms import InputForms
from utils.utils import button_attac

"""
if request.path == '/en/convert-case':
    links = {
        'nav_emoji': '/en/emoji',
        'nav_convert': '/en/convert-case',
        'nav_emoticon': '/en/emoticon'
        }
    transl = {
        'name_c': 'CONVERT CASE',
        'dev': 'Developed with \U0001F499 by Hireki',
        'desc': 'You can easily generate different styles of text, including UPPERCASE, lowercase and Title Case for fancy Youtube titles, and even cool fonts.'
        }
    return render(request, 'convert/en_convert_case.html', {
        'links': links, 'context': context, 'transl': transl, 'html_lang': html_lang})

elif request.path == '/pt/convert-case':
    links = {
        'nav_emoji': '/pt/emoji',
        'nav_convert': '/pt/convert-case',
        'nav_emoticon': '/pt/emoticon'
        }
    transl = {
        'name_c': 'LETRAS DIFERENTES',
        'dev':'Desenvolvido com \U0001F499 por Hireki',
        'desc': 'Converta seu texto com fontes de letras diferentes, legais e personalizadas, além de títulos para o Youtube automáticos em MAIÚSCULO, minúsculo e Título.'
        }
    return render(request, 'convert/pt_convert_case.html', {
        'links': links, 'context': context, 'transl': transl, 'html_lang': html_lang})

"""

class Convert(View):
    # TODO: template render improve
    # TODO: add max_lenght
    # TODO: remake redirect(redi)
    
    template_name = 'convert/en_convert_case.html'
    form_class = InputForms

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        return render(self.request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        self.context = {'form': form}

        if form.is_valid():
            form.cleaned = form.cleaned_data['input_txt']
        
        submit = (request.POST.get('submit'))
        form.treated_data = ''
        if submit:
            
            form.treated_data = button_attac(submit, form.cleaned)
            
        return render(self.request, self.template_name, self.context)
    

# def redi(request):
#     if request.path == '/en/':
#         return redirect('/en/convert-case')
#     elif request.path == '/pt/':
#         return redirect('/pt/convert-case')

#     html_lang = {
#         'hreflang0': '<link rel="alternate" hreflang="en" href="https://www.shadesapps.com/en/convert-case" />',
#         'hreflang1': '<link rel="alternate" hreflang="pt" href="https://www.shadesapps.com/pt/convert-case" />',
#         'hreflang2': '<link rel="alternate" hreflang="x-default" href="https://www.shadesapps.com/en/convert-case" />'
#         }
    
#     # Template render
#     if request.path == '/en/convert-case':
#         links = {
#             'nav_emoji': '/en/emoji',
#             'nav_convert': '/en/convert-case',
#             'nav_emoticon': '/en/emoticon'
#             }
#         transl = {
#             'name_c': 'CONVERT CASE',
#             'dev': 'Developed with \U0001F499 by Hireki',
#             'desc': 'You can easily generate different styles of text, including UPPERCASE, lowercase and Title Case for fancy Youtube titles, and even cool fonts.'
#             }
#         return render(request, 'convert/en_convert_case.html', {
#             'links': links, 'context': context, 'transl': transl, 'html_lang': html_lang})

#     elif request.path == '/pt/convert-case':
#         links = {
#             'nav_emoji': '/pt/emoji',
#             'nav_convert': '/pt/convert-case',
#             'nav_emoticon': '/pt/emoticon'
#             }
#         transl = {
#             'name_c': 'LETRAS DIFERENTES',
#             'dev':'Desenvolvido com \U0001F499 por Hireki',
#             'desc': 'Converta seu texto com fontes de letras diferentes, legais e personalizadas, além de títulos para o Youtube automáticos em MAIÚSCULO, minúsculo e Título.'
#             }
#         return render(request, 'convert/pt_convert_case.html', {
#             'links': links, 'context': context, 'transl': transl, 'html_lang': html_lang})

from django.shortcuts import render, redirect
from django.views.generic.base import View
from utils.utils import button_attac
from convert import forms


class Convert(View):
    template_name = 'convert/convertcase.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        if self.request.path == '/pt/convert-case/':
            self.template_name = 'convert/convertcase_pt.html'
    
        self.context = {
            'form': forms.InputForms(data=self.request.POST or None)
        }
        self.form = self.context['form']
        text = self.form.data.get('input_txt')

        
        submit_btn = (self.request.POST.get('submit'))
        self.form.new_data = ''
        
        if submit_btn:
            self.form.new_data = button_attac(submit_btn, text)

        self.renderizar = render(
            self.request, self.template_name, self.context
        )

    def get(self, request, *args, **kwargs):  
        return self.renderizar

    def post(self, request, *args, **kwargs):
        return self.renderizar

from django.shortcuts import render, redirect
from django.views.generic.base import View
from convert.forms import InputForms
from utils.utils import button_attac


class Convert(View):
    template_name = 'convert/convertcase.html'
    form_class = InputForms

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.form = self.form_class(self.request.POST or None)
        self.context = {'form':self.form}

        if self.request.path == '/pt/convert-case/':
            self.template_name = 'convert/convertcase_pt.html'
        
        self.renderizar = render(
            self.request, self.template_name, self.context
        )

    def get(self, request, *args, **kwargs):        
        return self.renderizar

    def post(self, request, *args, **kwargs):
        # TODO: Set a proper clean
        form_cleaned = self.form.data.get('input_txt')

        if len(form_cleaned) > 10000:
            form_cleaned = form_cleaned[:10000]
            
        submit = (request.POST.get('submit'))
        self.form.treated_data = ''

        if submit:
            self.form.treated_data = button_attac(submit, form_cleaned)
            
        return self.renderizar

from django.shortcuts import render, redirect
from django.views.generic.base import View
from convert.forms import InputForms
from utils.utils import button_attac


class Convert(View):
    template_name = 'convert/convertcase.html'
    form_class = InputForms

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        return render(self.request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        self.context = {'form': form}

        form_cleaned = form.data.get('input_txt')
        if len(form_cleaned) > 999:
            form_cleaned = form_cleaned[:999]
            
        submit = (request.POST.get('submit'))
        form.treated_data = ''
        if submit:
            form.treated_data = button_attac(submit, form_cleaned)
            
        return render(self.request, self.template_name, self.context)

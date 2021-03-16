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

        if form.is_valid():
            form.cleaned = form.cleaned_data['input_txt']
        
        submit = (request.POST.get('submit'))
        form.treated_data = ''
        if submit:
            
            form.treated_data = button_attac(submit, form.cleaned)
            
        return render(self.request, self.template_name, self.context)

    # TODO: add max_lenght
from django.shortcuts import render
from django.views.generic import View
from utils import convert


class ConvertCase(View):
    template_name = 'convertcase/convertcase.html'

    def setup(self, *args, **kwargs):
        self.context = {}
        return super().setup(*args, **kwargs)

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

    def post(self, *args, **kwargs):
        text_area_value = self.request.POST.get('text_area')
        button_value = self.request.POST.get('b_val')

        
        if len(text_area_value) > 2000:
            text_area_value = text_area_value[:2000]
            self.context['alert'] = 'warning'
            
            
        conv = convert.point_convert(button_value, text_area_value)
        self.context['textarearesponse'] = conv
    
        return render(self.request, self.template_name, self.context)

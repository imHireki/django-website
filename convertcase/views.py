from django_hosts.resolvers import reverse
from django.shortcuts import render
from django.views.generic import View
from utils import convert


class ConvertCase(View):
    
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        current_url = self.request.build_absolute_uri()

        if '//en.' in current_url:
            self.template_name = 'convertcase/en_convertcase.html'
        elif '//pt.' in current_url:
            self.template_name = 'convertcase/pt_convertcase.html'
        elif '//es.' in current_url:
            self.template_name = 'convertcase/es_convertcase.html'

        else:
            current_url = reverse('convertcase')

            if '//en.' in current_url:
                self.template_name = 'convertcase/en_convertcase.html'
            elif '//pt.' in current_url:
                self.template_name = 'convertcase/pt_convertcase.html'
            elif '//es.' in current_url:
                self.template_name = 'convertcase/es_convertcase.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

    def post(self, *args, **kwargs):
       
        text_area_value = self.request.POST.get('text_area')
        button_value = self.request.POST.get('b_val')

        self.context = {}
        
        if len(text_area_value) > 3000:
            text_area_value = text_area_value[:3000]
            self.context['alert'] = 'warning'
            
            
        conv = convert.point_convert(button_value, text_area_value)
        self.context['textarearesponse'] = conv
    
        return render(self.request, self.template_name, self.context)

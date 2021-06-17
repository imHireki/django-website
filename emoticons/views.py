from django_hosts.resolvers import reverse
from django.shortcuts import render
from django.views.generic import View


class Emoticons(View):

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        
        # current_url = reverse('convertcase')
        current_url = self.request.build_absolute_uri()
        
        if '//en.' in current_url:
            self.template_name = 'emoticons/en_emoticons.html'
        elif '//pt.' in current_url:
            self.template_name = 'emoticons/pt_emoticons.html'
        elif '//es.' in current_url:
            self.template_name = 'emoticons/es_emoticons.html'
    
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

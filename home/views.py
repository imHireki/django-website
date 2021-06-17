from django_hosts.resolvers import reverse
from django.shortcuts import render
from django.views.generic import View


class Home(View): 
    def setup(self, *args, **kwargs):
        # current_url = reverse('home')
        current_url = self.request.build_absolute_uri()

        if '//en.' in current_url:
            self.template_name = 'home/en_home.html'
        elif '//pt.' in current_url:
            self.template_name = 'home/pt_home.html'
        elif '//es.' in current_url:
            self.template_name = 'home/es_home.html'
        
        return super().setup(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

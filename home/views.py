from django.shortcuts import render
from django.views.generic.base import View


class Home(View):
    template_name = 'home/home.html'
    
    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name)

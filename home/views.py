from django.shortcuts import render, redirect
from django.views.generic import View


class Home(View): 
    template_name = 'home/home.html'
    
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

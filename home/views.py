from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View


class Home(View): 
    template_name = 'home/home.html'
    
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

    def post(self, *args, **kwargs):
        return render(self.request, self.template_name)

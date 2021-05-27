from django.shortcuts import render, HttpResponse
from django.views.generic import View


class Home(View): 
    def get(self, *args, **kwargs): return HttpResponse('Homee')

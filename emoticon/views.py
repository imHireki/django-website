from django.shortcuts import render
from django.views.generic.base import View


class Emoticon(View):
    template_name = 'emoticon/emoticon.html'
    
    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name)

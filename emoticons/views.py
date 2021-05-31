from django.shortcuts import render
from django.views.generic import View


class Emoticons(View):
    template_name = 'emoticons/emoticons.html'
    
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

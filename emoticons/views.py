from django.shortcuts import render
from django.views.generic import View


class Emoticons(View):
    template_name = 'emoticons/emoticons.html'
    
    def setup(self, *args, **kwargs):
        self.context = {}
        super().setup(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        return render(self.request, self.template_name, self.context)

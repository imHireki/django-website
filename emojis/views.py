from django.shortcuts import render
from django.views.generic import View
from data import emojidicts


class Emojis(View):
    template_name = 'emojis/emojis.html'
    
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        if '/pt/emojis/' in self.request.path:
            self.template_name = 'emojis/pt_emojis.html'

        self.context = {
            'faces': emojidicts.faces,
            'gestures': emojidicts.gestures,
            'people': emojidicts.people,
            'nature': emojidicts.nature,
            'food': emojidicts.food,
            'activity': emojidicts.activity,
            'travel': emojidicts.travel,
            'objects': emojidicts.objects,
            'symbols': emojidicts.symbols,
            'flags': emojidicts.flags,
            'newemojis': emojidicts.newemojis,
        }
        
    
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.context)

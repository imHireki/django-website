from django.shortcuts import render
from django.views.generic.base import View
from utils import emoji_dicts

class Emoji(View):
    template_name = 'emoji/emoji.html'
    
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.context = {
            'faces': emoji_dicts.faces,
            'gestures': emoji_dicts.gestures,
            'people': emoji_dicts.people,
            'nature': emoji_dicts.nature,
            'food': emoji_dicts.food,
            'activity': emoji_dicts.activity,
            'travel': emoji_dicts.travel,
            'objects': emoji_dicts.objects,
            'symbols': emoji_dicts.symbols,
            'flags': emoji_dicts.flags,
            'newemojis': emoji_dicts.newemojis,
            }
        
        if self.request.path == '/pt/emoji/':
            self.template_name = 'emoji/emoji_pt.html'
        
        self.renderizar = render(
            self.request, self.template_name, self.context
        )
        
    def get(self, request, *args, **kwargs):
        return self.renderizar

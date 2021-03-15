from django.shortcuts import render
from django.views.generic.base import View
from utils import emoji_dicts

class Emoji(View):
    template_name = 'emoji/emoji.html'
    
    def get(self, request, *args, **kwargs):
        emojis = {
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
        return render(self.request, self.template_name,  {'emojis': emojis})

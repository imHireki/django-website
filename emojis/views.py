from django_hosts.resolvers import reverse
from django.shortcuts import render
from django.views.generic import View
from data import emojidicts


class Emojis(View):
    
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        current_url = self.request.build_absolute_uri()

        if '//en.' in current_url:
            self.template_name = 'emojis/en_emojis.html'
        elif '//pt.' in current_url:
            self.template_name = 'emojis/pt_emojis.html'
        elif '//es.' in current_url:
            self.template_name = 'emojis/es_emojis.html'

        else:
            current_url = reverse('emojis') # //en.shadesapps.com/emojis/

            if '//en.' in current_url:
                self.template_name = 'emojis/en_emojis.html'
            elif '//pt.' in current_url:
                self.template_name = 'emojis/pt_emojis.html'
            elif '//es.' in current_url:
                self.template_name = 'emojis/es_emojis.html'

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

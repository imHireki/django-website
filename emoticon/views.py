from django.shortcuts import render
from django.views.generic.base import View


class Emoticon(View):
    template_name = 'emoticon/emoticon.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        if self.request.path == '/pt/emoticon/':
            self.template_name = 'emoticon/emoticon_pt.html'

        self.renderizar = render(self.request, self.template_name)

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name)

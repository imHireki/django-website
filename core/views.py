from django.views.generic import View
from django.urls import reverse
from django.shortcuts import redirect


class SwitchDarkMode(View):
    def dispatch(self, *args, **kwargs):
        super().dispatch(*args, **kwargs)

        http_referer = self.request.META.get(
            'HTTP_REFERER', reverse('home')
        )

        self.dark = self.request.POST.get('dark-mode')

        if not self.dark:
            if self.request.session.get('dark'):
                del self.request.session['dark']
        else:
            self.request.session['dark'] = 'checked' 

        self.request.session.save()
        return redirect(http_referer)

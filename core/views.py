from django_hosts import resolvers
from django.views.generic import TemplateView
from django.views.generic import View
from django.urls import reverse
from django.shortcuts import redirect, render


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


class Cover(TemplateView):
    template_name = 'core/cover.html'


class SiteMap(View):
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        current_subdomain = resolvers.reverse('sitemap')

        if '//en.' in current_subdomain:
            self.template_name = 'core/en/sitemap.xml'
        elif '//pt.' in current_subdomain:
            self.template_name = 'core/pt/sitemap.xml'
        elif '//es.' in current_subdomain:
            self.template_name = 'core/es/sitemap.xml'
        
    def get(self, *args, **kwargs):
        return render(
            self.request, self.template_name, content_type='text/xml'
        )


class RobotsTxt(View):
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        current_subdomain = resolvers.reverse('robots')

        if '//en.' in current_subdomain:
            self.template_name = 'core/en/robots.txt'
        elif '//pt.' in current_subdomain:
            self.template_name = 'core/pt/robots.txt'
        elif '//es.' in current_subdomain:
            self.template_name = 'core/es/robots.txt'
        
    def get(self, *args, **kwargs):
        return render(
            self.request, self.template_name, content_type='text/plain'
        )

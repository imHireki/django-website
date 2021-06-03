from django.views.generic import TemplateView


class Cover(TemplateView):
    template_name = 'cover/cover.html'

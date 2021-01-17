from django.shortcuts import render


def robots_txt(request):
    return render(request, 'robots.txt')

def sitemap_xml(request):
    return render(request, 'sitemap.xml')

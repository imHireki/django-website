"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core.views import robots_txt
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    path('', include('home.urls')),
    path('en/', include('convert.urls')),
    path('pt/', include('convert.urls')),
    path('en/convert-case', include('convert.urls')),
    path('pt/convert-case', include('convert.urls')),
    path('en/emoji', include('emoji.urls')),
    path('pt/emoji', include('emoji.urls')),
    path('en/emoticon', include('emoticon.urls')),
    path('pt/emoticon', include('emoticon.urls')),
    path('robots.txt', views.robots_txt, name='robots'),
    path('sitemap.xml', views.sitemap_xml, name='sitemap')
]

from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('home.urls')),
    path('sobre/', include('about.urls')),
    path('emojis/', include('emojis.urls')),
    path('emoticons/', include('emoticons.urls')),
    path('letras-diferentes/', include('convertcase.urls')),

    path('sitemap.xml', views.SiteMap.as_view(), name='sitemap'),
    path('robots.txt', views.RobotsTxt.as_view(), name='robots'),

    path('dark/', views.SwitchDarkMode.as_view(), name='dark'),
]

from django.urls import path
from .views import Cover
from . import views


urlpatterns = [
    path('', Cover.as_view(), name='cover'),
    path('sitemap.xml', views.SiteMap.as_view(), name='sitemap'),
    path('robots.txt', views.RobotsTxt.as_view(), name='robots'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.emoticon, name='emoticon')
]

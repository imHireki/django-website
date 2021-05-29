from django.urls import path
from .views import Emoticons


urlpatterns = [
    path('', Emoticons.as_view(), name='emoticons')
]

from django.urls import path
from .views import Emojis


urlpatterns = [
    path('', Emojis.as_view(), name='emojis')
]

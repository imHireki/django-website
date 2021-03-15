from django.urls import path
from .views import Emoji


urlpatterns = [
    path('', Emoji.as_view()),
]

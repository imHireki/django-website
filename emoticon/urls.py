from django.urls import path
from .views import Emoticon


urlpatterns = [
    path('', Emoticon.as_view())
]

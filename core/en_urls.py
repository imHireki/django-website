from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('home.urls'), name='home'),
    path('en/emojis/', include('emojis.urls')), # TODO: hm ? 
    path('en/emoticons/', include('emoticons.urls')),
    path('dark/', views.SwitchDarkMode.as_view(), name='dark'),
]

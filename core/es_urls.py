from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('home.urls')),
    path('emojis/', include('emojis.urls')),
    path('emoticons/', include('emoticons.urls')),
    path('letras-diferentes/', include('convertcase.urls')),
    path('dark/', views.SwitchDarkMode.as_view(), name='dark'),
]

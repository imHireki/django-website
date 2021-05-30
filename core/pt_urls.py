from django.urls import path, include


urlpatterns = [
    path('convert-case/', include('convertcase.urls')),
    path('pt/emojis/', include('emojis.urls'), name='aasdadaaa'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('letras-diferentes/', views.letras_diferentes, name='letrasDiferentes'),
]

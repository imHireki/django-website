from django.urls import path
from . import views


urlpatterns = [
    path('', views.ConvertCase.as_view(), name='convertcase')
]

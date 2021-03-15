from django.urls import path
from . import views


urlpatterns = [
    path('', views.Convert.as_view()),
]

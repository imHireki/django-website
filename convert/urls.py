from django.urls import path
from . import views


urlpatterns = [
    path('', views.redi, name='redi'),
    path('convert-case', views.convert, name='convert_case'),
]

from django.urls import path
from . import views


urlpatterns = [
    # path('', views.redi, name='redi'),
    path('convert-case', views.Convert.as_view()),
]

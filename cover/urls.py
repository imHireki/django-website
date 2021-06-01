from django.urls import path
from .views import Cover


urlpatterns = [
    path('', Cover.as_view(), name='cover')
]

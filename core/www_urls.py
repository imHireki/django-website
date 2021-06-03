from django.urls import path
from cover.views import Cover


urlpatterns = [
    path('', Cover.as_view(), name='cover')
]

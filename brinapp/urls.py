from django.urls import path
from brinapp.views import home

urlpatterns = [
    path('', home, name='home')
]

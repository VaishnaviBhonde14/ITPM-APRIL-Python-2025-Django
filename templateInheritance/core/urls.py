# from django.contrib import path
from django.urls import path
from .views import home, about

urlpatterns = [
    path('h/', home, name='home'),
    path('about/', about, name='about'),
]
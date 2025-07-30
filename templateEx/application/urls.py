from django.contrib import admin
from django.urls import path
from application.views import my_fun       # from .views import my_fun


urlpatterns = [
    path('ys/',my_fun)
]
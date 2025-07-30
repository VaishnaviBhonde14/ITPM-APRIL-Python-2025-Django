# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   path("itpre/" , views.fliter_demo, name="fliter_demo")
]
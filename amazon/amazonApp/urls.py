from django.contrib import admin
from django.urls import path
from .views import home,contact,product

urlpatterns = [
   path('h/', home),
   path('c/', contact),
   path('p/', product),

]

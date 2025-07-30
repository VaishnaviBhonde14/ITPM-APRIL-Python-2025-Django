from django.contrib import admin
from django.urls import path
from UserApp.views import my_user_view

urlpatterns = [
    path('user/',my_user_view, name='my_user_view')
]

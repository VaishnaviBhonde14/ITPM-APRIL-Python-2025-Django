from django.urls import path
from . import views

urlpatterns = [
   path('ys/', views.fliter_demo , name="filter_demo")

]

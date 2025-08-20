from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.profile, name='dashboard'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('verify_forgot_otp/', views.verify_forgot_otp, name='verify_forgot_otp'),

]
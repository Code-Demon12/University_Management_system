from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('verify-otp/', views.verify_otp),
]

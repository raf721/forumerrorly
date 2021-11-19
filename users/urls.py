"""Defines URL patterns for users"""
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'

urlpatterns = [
    # Login page
    url('login/', LoginView.as_view(template_name= 'users/login.html'),name='login'),
    # Registration page
    url(r'^register/$', views.register, name='register'),
]
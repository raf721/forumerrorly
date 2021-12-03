"""Defines URL patterns for users"""
from django.conf.urls import url
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView,PasswordChangeView,PasswordChangeDoneView
from django.urls.base import reverse_lazy
from . import views

app_name = 'users'

urlpatterns = [
    # Login page
    url('login/', LoginView.as_view(template_name= 'users/login.html'),name='login'),
    # Logout page
    url('logout/', views.logout_view, name='logout'),
    # Registration page
    url('^register/', views.register, name='register'),
    #Reset Password page
    url('password_reset_form/', PasswordResetView.as_view(template_name= 'users/password_reset_form.html', success_url = reverse_lazy('users:password_reset_done')), name='password_reset_form' ),
    #Reset Password Done page
    url('password_reset_done/', PasswordResetDoneView.as_view(template_name= 'users/password_reset_done.html'), name='password_reset_done' ),
]
from django.contrib.admin.options import csrf_protect_m
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordContextMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from django.conf import settings
from django.core.mail import send_mail
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def logout_view(request):
    """Log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

def register(request):
 """Register a new user."""
 if request.method != 'POST':
 # Display blank registration form.
    form = UserCreationForm()
 else:
    # Process completed form.
    form = UserCreationForm(data=request.POST)

 if form.is_valid():
    new_user = form.save()
 # Log the user in and then redirect to home page.
    authenticated_user = authenticate(username=new_user.username,
    password=request.POST['password1'])
    login(request, authenticated_user)
    return HttpResponseRedirect(reverse('users:login'))
    
 context = {'form': form}
 return render(request, 'users/register.html', context)


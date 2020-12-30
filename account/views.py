from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegistrationForm


class RegisterView(CreateView):
    model = get_user_model()
    form_class = RegistrationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('home-page')


class SigninView(LoginView):
    template_name = 'account/login.html'
    # success_url = reverse_lazy('home-page')

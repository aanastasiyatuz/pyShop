from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegistrationForm


class RegisterView(CreateView):
    model = User
    template_name = 'account/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')


class SighInView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('home')

from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.template.loader import get_template
from django.views.generic import TemplateView


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    succes_url = reverse_lazy("login")
    template = get_template('registration/register.html')
    # template_name = 'registration/register.html'


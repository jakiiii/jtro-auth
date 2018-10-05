from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib.messages.views import SuccessMessageMixin, messages

from .forms import UserLoginForm, UserRegistrationForm


# Create your views here.
class UserLoginView(FormView):
    from_class = UserLoginForm
    success_url = ''
    template_name = 'accounts/login.html'

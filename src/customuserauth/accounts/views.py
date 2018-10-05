from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin, messages

from .forms import UserLoginForm, UserRegistrationForm


# Create your views here.
class UserLoginView(FormView):
    form_class = UserLoginForm
    success_url = '/profile/'
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            login(self.request, user)
        else:
            messages.error(self.request, 'Username or Password is not valid!')
            return redirect('login')
        return super(UserLoginView, self).form_valid(form)


class UserRegistrationView(CreateView, SuccessMessageMixin):
    form_class = UserRegistrationForm
    template_name = 'accounts/registration.html'
    success_message = 'Registration successful.'
    success_url = '/login/'


def get_logout(request):
    logout(request)
    return redirect('home')

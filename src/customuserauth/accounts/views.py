from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.utils.http import is_safe_url
from django.contrib.messages.views import SuccessMessageMixin, messages

from .forms import UserLoginForm, UserRegistrationForm


# Create your views here.
class UserLoginView(FormView):
    form_class = UserLoginForm
    success_url = '/profile/'
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        next_ = self.request.GET.get('next')
        next_post = self.request.POST.get('next')
        redirect_path = next_ or next_post or None
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            if not user.is_active:
                messages.error(self.request, "This user is not active!")
                return super(UserLoginView, self).form_valid(form)
            login(self.request, user)
            if is_safe_url(redirect_path, self.request.get_host()):
                return redirect(redirect_path)
        else:
            messages.error(self.request, 'Username or Password is not valid!')
            return redirect('login')
        return super(UserLoginView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UserLoginView, self).get_context_data(**kwargs)
        context['title'] = 'Login'
        return context


class UserRegistrationView(SuccessMessageMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/registration.html'
    success_message = 'Registration successful.'
    success_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView, self).get_context_data(**kwargs)
        context['title'] = 'Registration'
        return context


class PasswordChangeView(FormView):
    def get_context_data(self, **kwargs):
        context = super(PasswordChangeView, self).get_context_data(**kwargs)
        context['title'] = 'Change Password'
        return context


def get_logout(request):
    logout(request)
    return redirect('home')

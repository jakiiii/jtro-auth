from django.shortcuts import render, reverse
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.forms import UserInfoChangeForm
from accounts.models import User


# Create your views here.
class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profiles/profile.html'

    def get_object(self, queryset=None):
        return self.request.user


class UserInfoUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserInfoChangeForm
    template_name = 'profiles/update_user_info.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Update Info"
        return context

    def get_success_url(self):
        return reverse('profile')

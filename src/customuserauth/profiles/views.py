from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ProfileTemplateView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'profiles/profile.html'

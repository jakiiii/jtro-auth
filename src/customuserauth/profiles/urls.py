from django.urls import path
from .views import ProfileTemplateView

urlpatterns = [
    path('profile/', ProfileTemplateView.as_view(), name='profile')
]
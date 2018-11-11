from django.urls import path

from .views import (
    ProfileView,
    UserInfoUpdateView
)


urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('update/', UserInfoUpdateView.as_view(), name='update-info'),
]

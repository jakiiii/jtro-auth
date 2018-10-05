from django.urls import path

from .views import (
    UserLoginView,
    UserRegistrationView,
    get_logout
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('logout/', get_logout, name='logout')
]

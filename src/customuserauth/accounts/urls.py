from django.urls import path

from .views import (
    UserLoginView,
    UserRegistrationView,
    AccountEmailActivateView,
    get_logout
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('email/confirmed/<key>/', AccountEmailActivateView.as_view(), name='email-activate'),
    path('email/resend-activation/', AccountEmailActivateView.as_view(), name='resend-activate'),
    path('logout/', get_logout, name='logout')
]

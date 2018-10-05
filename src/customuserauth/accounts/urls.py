from django.urls import path

from .views import (
    UserLoginView,
    get_logout
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', get_logout, name='logout')
]

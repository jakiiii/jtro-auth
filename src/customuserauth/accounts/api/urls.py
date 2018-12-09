from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import (
    APIAuthView,
    APIRegisterView
)


urlpatterns = [
    path('', APIAuthView.as_view(), name='api-login'),
    path('register/', APIRegisterView.as_view(), name='api-register'),
    path('jwt/', obtain_jwt_token),
    path('jwt/refresh/', refresh_jwt_token),
]

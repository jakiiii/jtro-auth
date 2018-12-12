from django.urls import path

from .views import UserDetailAPIView, UserListAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name='api-user-list'),
    path('<int:id>/', UserDetailAPIView.as_view(), name='api-user-detail'),
]

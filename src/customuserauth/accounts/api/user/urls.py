from django.urls import path

from .views import UserDetailAPIView

urlpatterns = [
    path('<int:id>/', UserDetailAPIView.as_view(), name='api-user-detail'),
]

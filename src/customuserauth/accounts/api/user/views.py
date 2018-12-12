from django.contrib.auth import get_user_model

from rest_framework import generics, permissions

from .serializers import UserListSerializer, UserDetailSerializer

User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_active=True)
    lookup_field = 'id'  # slug -> username


class UserListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserListSerializer
    queryset = User.objects.filter(is_active=True)
    search_fields = ['id', 'email', 'first_name', 'last_name']
    ordering_fields = ['id', 'email', 'timestamp']

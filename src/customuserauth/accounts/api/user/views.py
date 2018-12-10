from django.contrib.auth import get_user_model

from rest_framework import generics, permissions

from .serializers import UserDetailSerializer

User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_active=True)
    lookup_field = 'id'  # slug -> username

    # def get_serializer_context(self):
    #     return {'request': self.request}

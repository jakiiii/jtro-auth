from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    user_uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'uri',
            'user_uri',
        ]

    def get_uri(self, obj):
        return api_reverse("api-user-list", request=self.context.get('request'))

    def get_user_uri(self, obj):
        return api_reverse("api-user-detail", kwargs={"id": obj.id}, request=self.context.get('request'))


class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'uri',
        ]

    def get_uri(self, obj):
        return api_reverse("api-user-detail", kwargs={"id": obj.id}, request=self.context.get('request'))


class UserPublicDisplaySerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'uri',
        ]

    def get_uri(self, obj):
        return api_reverse("api-user-detail", kwargs={"id": obj.id}, request=self.context.get('request'))

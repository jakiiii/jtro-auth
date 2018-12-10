from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


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
        return "/api/users/{id}/".format(id=obj.id)


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
        return "/api/users/{id}/".format(id=obj.id)

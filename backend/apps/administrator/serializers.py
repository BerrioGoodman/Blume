from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AministratorModel

class AdministratorRegistroSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)

    class Meta:
        model = AministratorModel
        fields = ["username", "password", "email", "first_name", "last_name", "rol", "nivel_acceso"]

    def create(self, validated_data):
        username = validated_data.pop("username")
        password = validated_data.pop("password")
        email = validated_data.pop("email")
        first_name = validated_data.pop("first_name")
        last_name = validated_data.pop("last_name")

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        administrator = AministratorModel.objects.create(user=user, **validated_data)
        return administrator

class AdministratorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)

    class Meta:
        model = AministratorModel
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'rol', 'nivel_acceso']
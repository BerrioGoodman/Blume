from rest_framework import serializers
from django.contrib.auth.models import User
from .models import EstudianteModel

class EstudianteRegistroSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)

    class Meta:
        model = EstudianteModel
        fields = ["username", "password", "email", "first_name", "last_name", "carrera", "semestre"]

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

        estudiante = EstudianteModel.objects.create(user=user, **validated_data)
        return estudiante
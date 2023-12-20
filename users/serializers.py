from rest_framework import serializers
from rest_framework.validators import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import User


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create(email=validated_data["email"])

        user.set_password(validated_data["password1"])

        user.save()

        return user

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise ValidationError(
                code=status.HTTP_400_BAD_REQUEST, detail="Password must be the same"
            )

        return attrs


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        get_object_or_404(User, email=attrs["email"])
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise ValidationError(detail="Password must me the same")

        if len(attrs["password1"]) < 6 or len(attrs["password2"]) < 6:
            raise ValidationError(detail="min lenght 6")

        return attrs

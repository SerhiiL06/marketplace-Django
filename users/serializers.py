from rest_framework import serializers
from rest_framework.validators import ValidationError
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

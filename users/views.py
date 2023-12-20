from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import action
from .token import TokenOperations
from .models import User
from .serializers import (
    RegisterSerializer,
    ProfileSerializer,
    EmailSerializer,
    ChangePasswordSerializer,
)

token = TokenOperations()


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()

    @action(
        methods=["get"],
        detail=False,
        url_path="me",
        permission_classes=[permissions.IsAuthenticated],
    )
    def my_profile(self, request):
        current_user_serializer = ProfileSerializer(request.user)

        return Response({"users": current_user_serializer.data})

    @action(methods=["post"], detail=False, url_path="register")
    def register(self, request):
        data = RegisterSerializer(data=request.data)

        data.is_valid(raise_exception=True)

        data.save()

        return Response(data="Success register", status=status.HTTP_201_CREATED)

    @action(methods=["post"], detail=False, url_path="forgot-password")
    def foggot_password(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        access = token.create_token(serializer.validated_data.get("email"))
        return Response({"token": access})

    @action(
        methods=["post"],
        detail=False,
        url_name="change-password",
    )
    def change_password(self, request, *args, **kwargs):
        user_email = token.check_token(kwargs.get("token"))

        current_user = get_object_or_404(User, email=user_email)

        serializer = ChangePasswordSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        current_user.set_password(serializer.validated_data["password1"])

        current_user.save()

        return Response({"message": "well done"})

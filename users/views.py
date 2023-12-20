from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .models import User
from .serializers import RegisterSerializer


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()

    @action(methods=["post"], detail=False, url_path="register")
    def register(self, request):
        data = RegisterSerializer(data=request.data)

        data.is_valid(raise_exception=True)

        data.save()

        return Response(data="Success register", status=status.HTTP_201_CREATED)

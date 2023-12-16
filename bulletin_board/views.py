from rest_framework import viewsets
from .models import House, Announcement
from users.models import User
from . import serializers as local_ser
from .logic import get_type


class HouseViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = local_ser.AnnouncementSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return get_type(self.request.data["type"])

        return super().get_serializer_class()

    def perform_create(self, serializer):
        user = User.objects.get(id=1)
        return serializer.save(owner=user)

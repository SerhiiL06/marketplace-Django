from rest_framework import viewsets
from .models import House, Announcement
from users.models import User
from . import serializers as local_ser
from .logic import get_type, get_retrieve_type
from .fliters import AnnouncementFilter
from django_filters import rest_framework as filters


class HouseViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = local_ser.AnnouncementSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AnnouncementFilter

    def get_serializer_class(self):
        if self.action == "create":
            return get_type(self.request.data["type"])

        if self.action == "retrieve":
            return local_ser.RetrievehouseSerializer

        return super().get_serializer_class()

    def perform_create(self, serializer):
        user = User.objects.get(id=1)
        return serializer.save(owner=user)

from rest_framework import viewsets
from .models import House, Announcement
from users.models import User
from .serializers import AnnouncementSerializer, HouseSerializer


class HouseViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def perform_create(self, serializer):
        user = User.objects.get(id=1)
        return serializer.save(owner=user)

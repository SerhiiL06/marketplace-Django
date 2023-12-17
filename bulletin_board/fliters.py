from .models import Announcement
from django_filters import rest_framework as filters


class AnnouncementFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")
    title = filters.Filter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Announcement
        fields = ["title", "price", "type", "town"]

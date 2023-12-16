from rest_framework import serializers
from .models import House, Announcement, Work
from django.utils import timezone


class HouseSerializer(serializers.ModelSerializer):
    area = serializers.IntegerField(required=False)
    rooms = serializers.IntegerField(required=False)

    class Meta:
        model = House
        fields = ["area", "rooms"]


class WorkSerializer(serializers.ModelSerializer):
    calary = serializers.IntegerField(required=False)
    type_of_work = serializers.CharField(required=False)

    class Meta:
        model = Work
        fields = ["calary", "type_of_work"]


class AnnouncementSerializer(serializers.ModelSerializer):
    created = serializers.HiddenField(default=timezone.now)
    work = serializers.CharField(read_only=True)
    house = serializers.CharField(read_only=True)
    calary = serializers.IntegerField(write_only=True)
    type_of_work = serializers.CharField(write_only=True)

    class Meta:
        model = Announcement
        fields = [
            "title",
            "description",
            "price",
            "image",
            "created",
            "type",
            "town",
            "house",
            "work",
            "calary",
            "type_of_work",
        ]

    def create(self, validated_data):
        calary = validated_data.pop("calary", None)
        type_of_work = validated_data.pop("type_of_work", None)
        ann = Announcement.objects.create(**validated_data)

        if ann.type == "work":
            Work.objects.create(
                announcement=ann,
                calary=calary,
                type_of_work=type_of_work,
            )

        return ann

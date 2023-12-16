from rest_framework import serializers
from .models import House, Announcement, Work, Car, Other
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
    class Meta:
        model = Announcement
        fields = ["title", "description", "price", "image", "created", "type", "town"]


class CreateHouseSerializer(AnnouncementSerializer):
    rooms = serializers.IntegerField(write_only=True)
    area = serializers.FloatField(write_only=True)

    class Meta:
        model = Announcement
        fields = AnnouncementSerializer.Meta.fields + ["rooms", "area"]

    def create(self, validated_data):
        rooms = validated_data.pop("rooms", None)
        area = validated_data.pop("area", None)

        ann = Announcement.objects.create(**validated_data)

        House.objects.create(announcement=ann, rooms=rooms, area=area)

        return ann


class CreateWorkSerializer(AnnouncementSerializer):
    calary = serializers.IntegerField(write_only=True)
    type_of_work = serializers.CharField(write_only=True)

    class Meta:
        model = Announcement
        fields = AnnouncementSerializer.Meta.fields + ["calary", "type_of_work"]

    def create(self, validated_data):
        calary = validated_data.get("calary", None)
        type_of_work = validated_data.get("type_of_work", None)

        ann = Announcement.objects.create(**validated_data)

        Work.objects.create(announcement=ann, calary=calary, type_of_work=type_of_work)

        return ann


class CreateCarSerializer(AnnouncementSerializer):
    brand = serializers.CharField(write_only=True)
    year = serializers.FloatField(write_only=True)
    engine_power = serializers.FloatField(write_only=True)
    color = serializers.FloatField(write_only=True, required=False)
    status = serializers.CharField(write_only=True, default="in_use")

    class Meta:
        model = Announcement
        fields = AnnouncementSerializer.Meta.fields + [
            "brand",
            "year",
            "engine_power",
            "color",
            "status",
        ]

    def create(self, validated_data):
        data = {
            "brand": validated_data.pop("brand", None),
            "year": validated_data.pop("year", None),
            "engine_power": validated_data.pop("engine_power", None),
            "color": validated_data.pop("color", None),
            "status": validated_data.pop("status", None),
        }

        ann = Announcement.objects.create(**validated_data)

        print("I'm here")

        Car.objects.create(announcement=ann, **data).save()

        return ann


class CreateOtherSerializer(AnnouncementSerializer):
    def create(self, validated_data):
        instance = Announcement.objects.create(**validated_data)

        Other.objects.create(announcement=instance)
        return instance

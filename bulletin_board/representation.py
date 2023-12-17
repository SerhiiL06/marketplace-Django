from rest_framework import serializers
from .models import Work, House, Car, Other


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class OtherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Other
        fields = "__all__"

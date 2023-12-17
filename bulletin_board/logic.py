from . import serializers
from rest_framework.response import Response
from rest_framework import status


def get_type(type):
    if type == "house":
        return serializers.CreateHouseSerializer
    elif type == "work":
        return serializers.CreateWorkSerializer
    elif type == "car":
        return serializers.CreateCarSerializer
    elif type == "other":
        return serializers.CreateOtherSerializer

    return Response(data="incorrect type!", status=status.HTTP_400_BAD_REQUEST)


def get_retrieve_type(type):
    if type == "house":
        return serializers.RetrievehouseSerializer
    elif type == "work":
        return serializers.CreateWorkSerializer
    elif type == "car":
        return serializers.CreateCarSerializer
    elif type == "other":
        return serializers.CreateOtherSerializer

    return Response(data="incorrect type!", status=status.HTTP_400_BAD_REQUEST)

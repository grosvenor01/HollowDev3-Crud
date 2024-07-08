from rest_framework import serializers
from .models import *



class power_serializer(serializers.ModelSerializer):
    class Meta:
        model = power
        fields="__all__"

class GameChar_serializer(serializers.ModelSerializer):
    power = power_serializer(many=True)
    class Meta:
        model = gameCarecters
        fields = "__all__"

class GameChar2_serializer(serializers.ModelSerializer):
    class Meta:
        model = gameCarecters
        fields = "__all__"
from rest_framework import serializers
from . import models


class ApplyAdoptionSerializers(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = models.ApplyAdoption
        fields = '__all__'


class ApplyCareSerializers(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = models.ApplyCare
        fields = '__all__'


class ApplyMoveSerializers(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = models.ApplyMove
        fields = '__all__'

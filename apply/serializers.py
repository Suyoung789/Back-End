from rest_framework import serializers
from . import models


class ApplyAdoptionSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = models.ApplyAdoption
        fields = '__all__'


class ApplyAdoptionRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApplyAdoption
        fields = '__all__'


class ApplyCareSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = models.ApplyCare
        fields = '__all__'


class ApplyCareRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApplyCare
        fields = '__all__'


class ApplyMoveSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = models.ApplyMove
        fields = '__all__'


class ApplyMoveRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApplyMove
        fields = '__all__'

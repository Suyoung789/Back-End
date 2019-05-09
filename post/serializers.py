from rest_framework import serializers
from . import models


class AdoptionListSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = models.Adoption
        fields = '__all__'


class AdoptionRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Adoption
        fields = '__all__'


class CareListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = models.Care
        fields = '__all__'


class CareRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Care
        fields = '__all__'


class MoveListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = models.Move
        fields = '__all__'


class MoveRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Move
        fields = '__all__'


class ReportListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = models.Report
        fields = '__all__'


class ReportRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        fields = '__all__'


class FindListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = models.Find
        fields = '__all__'


class FindRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Find
        fields = '__all__'


class CommunityListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = models.Community
        fields = '__all__'


class CommunityRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Community
        fields = '__all__'

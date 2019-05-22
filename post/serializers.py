from rest_framework import serializers

from . import models


class AdoptionListSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = models.Adoption
        fields = ('title', 'content', 'creation_date', 'post_id',  'author', 'image', 'sex')


class AdoptionRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Adoption
        fields = '__all__'


class CareListSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = models.Care
        fields = '__all__'


class CareRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Care
        fields = '__all__'


class MoveListSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = models.Move
        fields = '__all__'


class MoveRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Move
        fields = '__all__'


class ReportListSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = models.Report
        fields = '__all__'


class ReportRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        fields = '__all__'


class FindListSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = models.Find
        fields = '__all__'


class FindRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Find
        fields = '__all__'


class CommunityListSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = models.Community
        fields = '__all__'


class CommunityRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Community
        fields = '__all__'

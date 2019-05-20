from rest_framework import serializers
from . import models


class CommentAdoptionSerializers(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = models.AdoptionComment
        fields = '__all__'


class CommentCareSerializers(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = models.CareComment
        fields = '__all__'


class CommentMoveSerializers(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = models.MoveComment
        fields = '__all__'


class CommentFindSerializers(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = models.FindComment
        fields = '__all__'


class CommentReportSerializers(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = models.ReportComment
        fields = '__all__'


class CommentCommunitySerializers(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = models.CommunityComment
        fields = '__all__'

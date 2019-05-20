from rest_framework import serializers
from . import models


class CommentSerializers(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = models.Comment
        fields = '__all__'

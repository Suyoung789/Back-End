from rest_framework import serializers
from . import models


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username', 'name', 'password', 'pet')

    def create(self, validated_data):
        user = models.User(
            username=validated_data['username'],
            name=validated_data['name'],
            pet=validated_data['pet']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
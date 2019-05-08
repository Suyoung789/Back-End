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

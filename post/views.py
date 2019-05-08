from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers


class AdoptionListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.AdoptionListSerializers
    queryset = models.Adoption.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdoptionRetrieveView(viewsets.generics.RetrieveDestroyAPIView):
    serializer_class = serializers.AdoptionRetrieveSerializer
    queryset = models.Adoption.objects.all()


class CareListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.CareListSerializer
    queryset = models.Care.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CareRetrieveView(viewsets.generics.RetrieveDestroyAPIView):
    serializer_class = serializers.CareRetrieveSerializer
    queryset = models.Care.objects.all()

from rest_framework import viewsets

from . import models
from . import serializers
from post.models import Adoption, Care, Move


class ApplyAdoptionListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.ApplyAdoptionSerializers
    queryset = models.ApplyAdoption.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Adoption.objects.get(post_id=self.kwargs['pk']))


class ApplyMoveListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.ApplyMoveSerializers
    queryset = models.ApplyMove.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Move.objects.get(post_id=self.kwargs['pk']))


class ApplyCareListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.ApplyCareSerializers
    queryset = models.ApplyCare.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Care.objects.get(post_id=self.kwargs['pk']))
from rest_framework import viewsets

from . import models
from . import serializers
from post.models import Adoption, Care, Move


class ApplyAdoptionListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.ApplyAdoptionSerializer
    queryset = models.ApplyAdoption.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Adoption.objects.get(post_id=self.kwargs['post_id']))


class ApplyAdoptionRetrieveView(viewsets.generics.RetrieveDestroyAPIView):
    serializer_class = serializers.ApplyAdoptionRetrieveSerializer
    queryset = models.ApplyAdoption.objects.all()


class ApplyMoveListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.ApplyMoveSerializer
    queryset = models.ApplyMove.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Move.objects.get(post_id=self.kwargs['post_id']))


class ApplyCareRetrieveView(viewsets.generics.RetrieveDestroyAPIView):
    serializer_class = serializers.ApplyCareRetrieveSerializer
    queryset = models.ApplyCare.objects.all()


class ApplyCareListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.ApplyCareSerializer
    queryset = models.ApplyCare.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Care.objects.get(post_id=self.kwargs['post_id']))


class ApplyMoveRetrieveView(viewsets.generics.RetrieveDestroyAPIView):
    serializer_class = serializers.ApplyMoveRetrieveSerializer
    queryset = models.ApplyMove.objects.all()

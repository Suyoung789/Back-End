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


class MoveListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.MoveListSerializer
    queryset = models.Move.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MoveRetrieveView(viewsets.generics.RetrieveDestroyAPIView):
    serializer_class = serializers.MoveListSerializer
    queryset = models.Move.objects.all()


class ReportListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.ReportListSerializer
    queryset = models.Report.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ReportRetrieveView(viewsets.generics.RetrieveDestroyAPIView):
    serializer_class = serializers.ReportRetrieveSerializers
    queryset = models.Report.objects.all()


class FindListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.FindListSerializer
    queryset = models.Find.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FindRetrieveView(viewsets.generics.RetrieveDestroyAPIView):
    serializer_class = serializers.FindRetrieveSerializers
    queryset = models.Find.objects.all()


class CommunityListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.CommunityListSerializer
    queryset = models.Community.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommunityRetrieveView(viewsets.generics.RetrieveDestroyAPIView):
    serializer_class = serializers.CommunityRetrieveSerializers
    queryset = models.Community.objects.all()


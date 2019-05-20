from rest_framework import viewsets

from . import models
from . import serializers
from post.models import Adoption, Care, Move, Find, Report, Community


class CommentAdoptionListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.CommentAdoptionSerializers
    queryset = models.AdoptionComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Adoption.objects.get(post_id=self.kwargs['pk']))

    def get_queryset(self):
        pk = self.kwargs['pk']
        return models.AdoptionComment.objects.filter(post=pk)


class CommentCareListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.CommentCareSerializers
    queryset = models.CareComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Care.objects.get(post_id=self.kwargs['pk']))

    def get_queryset(self):
        pk = self.kwargs['pk']
        return models.CareComment.objects.filter(post=pk)


class CommentMoveListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.CommentMoveSerializers
    queryset = models.AdoptionComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Move.objects.get(post_id=self.kwargs['pk']))

    def get_queryset(self):
        pk = self.kwargs['pk']
        return models.MoveComment.objects.filter(post=pk)


class CommentFindListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.CommentFindSerializers
    queryset = models.FindComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Find.objects.get(post_id=self.kwargs['pk']))

    def get_queryset(self):
        pk = self.kwargs['pk']
        return models.FindComment.objects.filter(post=pk)


class CommentReportListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.CommentReportSerializers
    queryset = models.AdoptionComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Report.objects.get(post_id=self.kwargs['pk']))

    def get_queryset(self):
        pk = self.kwargs['pk']
        return models.ReportComment.objects.filter(post=pk)


class CommentCommunityListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.CommentCommunitySerializers
    queryset = models.AdoptionComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Community.objects.get(post_id=self.kwargs['pk']))

    def get_queryset(self):
        pk = self.kwargs['pk']
        return models.CommunityComment.objects.filter(post=pk)
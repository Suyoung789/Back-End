from rest_framework import viewsets

from . import models
from . import serializers
from post.models import Adoption, Care, Move, Find, Report, Community


class CommentAdoptionListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.CommentAdoptionSerializer
    queryset = models.AdoptionComment.objects.all().order_by('-comment_id')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Adoption.objects.get(post_id=self.kwargs['post_id']))

    def get_queryset(self):
        pk = self.kwargs['post_id']
        return models.AdoptionComment.objects.filter(post=pk)


class CommentCareListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.CommentCareSerializer
    queryset = models.CareComment.objects.all().order_by('-comment_id')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Care.objects.get(post_id=self.kwargs['post_id']))

    def get_queryset(self):
        pk = self.kwargs['post_id']
        return models.CareComment.objects.filter(post=pk)


class CommentMoveListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.CommentMoveSerializer
    queryset = models.AdoptionComment.objects.all().order_by('-comment_id')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Move.objects.get(post_id=self.kwargs['post_id']))

    def get_queryset(self):
        pk = self.kwargs['post_id']
        return models.MoveComment.objects.filter(post=pk)


class CommentFindListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.CommentFindSerializer
    queryset = models.FindComment.objects.all().order_by('-comment_id')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Find.objects.get(post_id=self.kwargs['post_id']))

    def get_queryset(self):
        pk = self.kwargs['post_id']
        return models.FindComment.objects.filter(post=pk)


class CommentReportListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.CommentReportSerializer
    queryset = models.AdoptionComment.objects.all().order_by('-comment_id')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Report.objects.get(post_id=self.kwargs['post_id']))

    def get_queryset(self):
        pk = self.kwargs['post_id']
        return models.ReportComment.objects.filter(post=pk)


class CommentCommunityListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.CommentCommunitySerializer
    queryset = models.AdoptionComment.objects.all().order_by('-comment_id')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Community.objects.get(post_id=self.kwargs['post_id']))

    def get_queryset(self):
        pk = self.kwargs['post_id']
        return models.CommunityComment.objects.filter(post=pk)

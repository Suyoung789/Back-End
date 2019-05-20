from rest_framework import viewsets
from django.apps import apps
from . import models
from . import serializers
from post.models import Post


class CommentListView(viewsets.generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializers
    queryset = models.Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=Post.objects.get(post_id=self.kwargs['pk']))

    def get_queryset(self):
        post = self.kwargs['pk']
        return models.Comment.objects.filter(post=post)

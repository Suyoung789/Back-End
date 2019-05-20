from django.db import models
from post import models as model
from django.conf import settings


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username')
    content = models.TextField()

    class Meta:
        abstract = True


class AdoptionComment(Comment):
    post = models.ForeignKey(model.Adoption, on_delete=models.CASCADE, to_field='post_id')


class CareComment(Comment):
    post = models.ForeignKey(model.Care, on_delete=models.CASCADE, to_field='post_id')


class MoveComment(Comment):
    post = models.ForeignKey(model.Move, on_delete=models.CASCADE, to_field='post_id')


class ReportComment(Comment):
    post = models.ForeignKey(model.Report, on_delete=models.CASCADE, to_field='post_id')


class FindComment(Comment):
    post = models.ForeignKey(model.Find, on_delete=models.CASCADE, to_field='post_id')


class CommunityComment(Comment):
    post = models.ForeignKey(model.Community, on_delete=models.CASCADE, to_field='post_id')


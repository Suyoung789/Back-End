from django.db import models
from django.conf import settings
from post.models import Adoption, Care, Move


class Apply(models.Model):
    apply_id = models.AutoField(primary_key=True)
    creation_date = models.DateField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current_location = models.CharField(max_length=40)
    content = models.TextField()

    class Meta:
        abstract = True


class ApplyAdoption(Apply):
    post = models.ForeignKey(Adoption, on_delete=models.CASCADE, to_field='post_id')


class ApplyCare(Apply):
    post = models.ForeignKey(Care, on_delete=models.CASCADE, to_field='post_id')


class ApplyMove(Apply):
    post = models.ForeignKey(Move, on_delete=models.CASCADE, to_field='post_id')

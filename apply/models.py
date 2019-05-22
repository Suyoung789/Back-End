from django.db import models
from django.conf import settings
from post.models import Adoption, Care, Move


class Apply(models.Model):
    apply_id = models.AutoField(primary_key=True)
    creation_date = models.DateField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    kakao_id = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=40)

    class Meta:
        abstract = True


class ApplyAdoption(Apply):
    post = models.ForeignKey(Adoption, on_delete=models.CASCADE, to_field='post_id')
    current_location = models.CharField(max_length=50)


class ApplyCare(Apply):
    post = models.ForeignKey(Care, on_delete=models.CASCADE, to_field='post_id')
    possible_month = models.IntegerField()
    current_location = models.CharField(max_length=40)


class ApplyMove(Apply):
    post = models.ForeignKey(Move, on_delete=models.CASCADE, to_field='post_id')
    possible_time = models.IntegerField()

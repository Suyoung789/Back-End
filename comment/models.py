from django.db import models
from post import models as model
from django.conf import settings


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(model.Post, on_delete=models.CASCADE, to_field='post_id')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username')
    content = models.TextField()

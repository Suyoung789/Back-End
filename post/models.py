from django.db import models

from django.conf import settings


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    content = models.TextField()
    creation_date = models.DateField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username')
    image = models.ImageField(default='media/test.png', null=True, blank=True)

    class Meta:
        abstract = True


class Adoption(Post):
    sex = models.CharField(max_length=2)
    age = models.CharField(max_length=10, default=0)
    kind = models.TextField(default=0)


class Care(Post):
    current_location = models.CharField(max_length=40)
    sex = models.CharField(max_length=2)
    kind = models.TextField(default=0)
    age = models.CharField(max_length=10, default=0)


class Move(Post):
    current_location = models.CharField(max_length=40)
    destination_location = models.CharField(max_length=40)
    sex = models.CharField(max_length=2)
    kind = models.TextField(default=0)
    age = models.CharField(max_length=10, default=0)


class Report(Post):
    current_location = models.CharField(max_length=40)


class Find(Post):
    sex = models.CharField(max_length=2)
    pet_name = models.CharField(max_length=20)
    kind = models.TextField(default=0)


class Community(Post):
    pass


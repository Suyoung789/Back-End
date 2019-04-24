from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=20)
    pet = models.IntegerField()
    isAdmin = models.BooleanField(default=False)


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    content = models.TextField()
    creation_date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Adoption(Post):
    sex = models.CharField(max_length=2)


class Care(Post):
    current_location = models.CharField(max_length=40)
    sex = models.CharField(max_length=2)


class Move(Post):
    current_location = models.CharField(max_length=40)
    destination_location = models.CharField(max_length=40)
    sex = models.CharField(max_length=2)


class Report(Post):
    current_location = models.CharField(max_length=40)


class Find(Post):
    sex = models.CharField(max_length=2)
    pet_name = models.CharField(max_length=20)


class Community(Post):
    pass


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Apply(models.Model):
    apply_id = models.AutoField(primary_key=True)
    creation_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_location = models.CharField(max_length=40)
    content = models.TextField()


class ApplyAdoption(Apply):
    post = models.ForeignKey(Adoption, on_delete=models.CASCADE)


class ApplyCare(Apply):
    post = models.ForeignKey(Care, on_delete=models.CASCADE)


class ApplyMove(Apply):
    post = models.ForeignKey(Move, on_delete=models.CASCADE)

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy
from django.contrib.auth.validators import UnicodeUsernameValidator


class User(AbstractUser):
    username = models.CharField(
        gettext_lazy('username'),
        max_length=150,
        primary_key=True,
        help_text=gettext_lazy('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': gettext_lazy("A user with that username already exists."),
        },
    )
    name = models.CharField(max_length=20)
    pet = models.IntegerField()
    isAdmin = models.BooleanField(default=False)


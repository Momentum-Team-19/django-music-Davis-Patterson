from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Album(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def archive(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class User(AbstractUser):
    pass

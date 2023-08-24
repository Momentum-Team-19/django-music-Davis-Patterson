from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Artist(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def archive(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class User(AbstractUser):
    pass

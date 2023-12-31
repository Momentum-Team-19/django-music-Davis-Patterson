from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import datetime
import os


class Artist(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='albums')
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name="albums", default="default")
    title = models.CharField(max_length=200, default='[TITLE]')
    released = models.CharField(max_length=20, default='[N/A]')
    bio = models.CharField(max_length=650, default='[N/A]')
    album_art = models.ImageField(
        upload_to='media/',
        default='media/unavailable.jpg'
    )
    created_date = models.DateTimeField(default=timezone.now)

    def archive(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class User(AbstractUser):
    favorites = models.ManyToManyField('Album', related_name='favUsers')

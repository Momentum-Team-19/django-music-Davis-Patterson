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
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name="albums", default="default")
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    album_art = models.ImageField(
        upload_to='media/',
        default='/Users/davis/Momentum/Phase2/django-music-Davis-Patterson/django_music/static/album_art/unavailable.jpg'
    )

    def archive(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class User(AbstractUser):
    # favorites = models.ManyToManyField('Album')
    pass


class Favorite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favorites")
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="favorite_albums")
    is_favorite = models.BooleanField(default=False)

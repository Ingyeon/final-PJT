from django.conf import settings
from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100, null=True)
    release_date = models.DateField(null=True)
    popularity = models.FloatField(null=True)
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=200, null=True)
    movie_id = models.IntegerField(primary_key=True)
    genre_id = models.IntegerField(null=True)
    movie_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movie')

class Similar(models.Model):
    title = models.CharField(max_length=100, null=True)
    release_date = models.DateField(null=True)
    popularity = models.FloatField(null=True)
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=200, null=True)
    movie_id = models.IntegerField(primary_key=True)
    genre_id = models.IntegerField(null=True)
    movie_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='similar')



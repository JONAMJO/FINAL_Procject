from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=30)


class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=140)
    summary = models.TextField()
    director = models.CharField(max_length=45)
    genres = models.ManyToManyField(Genre, related_name='movies')
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_movies', blank=True)


class Review(models.Model):
    comment = models.CharField(max_length=150)
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

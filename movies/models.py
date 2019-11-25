from datetime import datetime
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator



class Hashtag(models.Model):
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content
    

class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Movie(models.Model):
    actor = models.CharField(max_length=150, default="", blank=True)
    director = models.CharField(max_length=150, default="", blank=True)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    image = models.URLField(max_length=200, default="", blank=True)
    link = models.URLField(max_length=200, default="", blank=True)
    title = models.CharField(max_length=150)
    pubDate = models.IntegerField(blank=True)
    subtitle = models.CharField(max_length=150, default="", blank=True)
    userRating = models.FloatField(default=0)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movies:detail", kwargs={"movie_pk": self.pk})
    

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    review = models.CharField(max_length=150)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    class Meta:
        ordering = ('-pk',)


    def __str__(self):
        return {self.score}, {self.comment}
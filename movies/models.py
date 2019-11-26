from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from datetime import datetime
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
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150, default="", blank=True)
    image = models.URLField(max_length=200, default="", blank=True)
    pubDate = models.IntegerField(blank=True)
    userRating = models.FloatField(default=0)
    link = models.URLField(max_length=200, default="", blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    director = models.CharField(max_length=150, default="", blank=True)
    actor = models.CharField(max_length=150, default="", blank=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("movies:detail", kwargs={"movie_pk": self.pk})
    

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    review = models.CharField(max_length=150)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)


    def __str__(self):
        return {self.score}, {self.review}

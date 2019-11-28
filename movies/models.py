from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class Cast(models.Model):
    peopleNm = models.CharField(max_length=150)
    img_url = models.CharField(max_length=150, default="", blank=True)

    def __str__(self):
        return self.peopleNm


class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150, default="", blank=True)
    poster_url = models.CharField(max_length=150, default="", blank=True)
    open_date = models.CharField(max_length=50, default="", blank=True)
    audience = models.IntegerField(default=0, blank=True)
    show_time = models.IntegerField(default=0, blank=True)
    user_rating = models.FloatField(default=0, blank=True)
    nation = models.CharField(max_length=30, default="", blank=True)
    watch_grade = models.CharField(max_length=30, default="", blank=True)
    description = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    genre = models.ManyToManyField(Genre, related_name='movie_genres', blank=True)
    director = models.CharField(max_length=150, default="", blank=True)
    actor = models.ForeignKey(Cast, related_name='movie_casts', blank=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("movies:detail", kwargs={"movie_pk": self.pk})
    

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    review = models.CharField(max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)


    def __str__(self):
        return {self.score}, {self.review}

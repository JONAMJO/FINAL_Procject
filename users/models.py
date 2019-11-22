from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    is_staff = models.IntegerField()
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')

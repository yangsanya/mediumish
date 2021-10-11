from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)

    avatar = models.ImageField(default='img/avatar.jpg', upload_to='users/')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

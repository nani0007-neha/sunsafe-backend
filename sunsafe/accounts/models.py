from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username


class SkinTone(models.Model):
    tone_name = models.CharField(max_length=50, unique=True)
    uv_absorption_factor = models.FloatField()

    def __str__(self):
        return self.tone_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skin_tone = models.ForeignKey(SkinTone, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username

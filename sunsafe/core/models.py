from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


# ---- User & skin tone ----

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


# ---- UV tables ----

class UVIndexRecord(models.Model):
    location = models.CharField(max_length=100)
    uv_level_index = models.FloatField()
    timestamp = models.DateTimeField()

    class Meta:
        indexes = [
            models.Index(fields=["location", "timestamp"]),
        ]

    def __str__(self):
        return f"{self.location} @ {self.timestamp} = {self.uv_level_index}"


class UVHistory(models.Model):
    location = models.CharField(max_length=100)
    uv_level = models.FloatField()
    timestamp = models.DateTimeField()
    source = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=["location", "timestamp"]),
        ]

    def __str__(self):
        return f"{self.location} @ {self.timestamp} = {self.uv_level} ({self.source})"


class ClothingRecommendation(models.Model):
    uv_level = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return f"UV {self.uv_level}: {self.description[:30]}..."
    
class Reminder(models.Model):
    REMINDER_TYPES = [
        ("SUNSCREEN", "Sunscreen"),
        ("CLOTHING", "Clothing"),
        ("SHADE", "Shade"),
        ("GENERAL", "General"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("SENT", "Sent"),
        ("DISMISSED", "Dismissed"),
    ]

    user = models.ForeignKey("User", on_delete=models.CASCADE)
    reminder_time = models.DateTimeField()
    reminder_type = models.CharField(max_length=20, choices=REMINDER_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")

    def __str__(self):
        return f"{self.user.username} @ {self.reminder_time} ({self.reminder_type})"


class SkinCancerStats(models.Model):
    year = models.IntegerField()
    age_group = models.CharField(max_length=50)
    skin_tone = models.ForeignKey("SkinTone", on_delete=models.SET_NULL, null=True)
    incidence_rate = models.FloatField()
    mortality_rate = models.FloatField()
    source = models.CharField(max_length=255)

    class Meta:
        indexes = [
            models.Index(fields=["year", "age_group"]),
        ]

    def __str__(self):
        return f"{self.year} {self.age_group} ({self.skin_tone})"


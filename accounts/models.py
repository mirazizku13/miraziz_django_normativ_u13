from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models



class UserRole(models.TextChoices):
    Poster = "Poster"
    Moderator = "Moderator"


class User(AbstractUser):
    role = models.CharField(max_length=10, choices=UserRole.choices, default=UserRole.Poster)
    phone_number = models.CharField(max_length=11, blank=True)
    email = models.EmailField(max_length=254, unique=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']
    class Meta:
        db_table = 'users'

# Create your models here.

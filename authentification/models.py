from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    on_trial = models.BooleanField(default=True)

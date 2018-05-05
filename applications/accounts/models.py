import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    country = models.CharField(max_length=255, default='', blank=True)
    city = models.CharField(max_length=255, default='', blank=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

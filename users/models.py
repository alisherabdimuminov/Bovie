from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True, null=False, blank=False, verbose_name="Telefon raqami")
    first_name = models.CharField(max_length=50, verbose_name="Ismi")
    last_name = models.CharField(max_length=50, verbose_name="Familiyasi")

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

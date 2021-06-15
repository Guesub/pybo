from django.contrib.auth.models import AbstractUser

from django.db import models
from . import managers

# Create your models here.

class CustomUser(AbstractUser):

    """ Custom User model """

    LOGIN_EMAIL = "email"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_KAKAO, "Kakao"),
    )

    login_method = models.CharField(
        max_length=6, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )

    access_token = models.CharField(max_length=100, null=True, blank=True)
    avatar = models.CharField(max_length=200, null=True, blank=True, default=None)

    objects = managers.CustomUserModelManager()
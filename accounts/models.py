from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username=None
    first_name=None
    last_name=None
    name=models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(_('email address'), unique=True)
    address = models.TextField(max_length=500)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

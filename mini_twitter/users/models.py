#from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=150)
    email = models.EmailField()
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user_name
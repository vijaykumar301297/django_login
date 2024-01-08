from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class Signup(AbstractBaseUser):
    first_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'signUp'

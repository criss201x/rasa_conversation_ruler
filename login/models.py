from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.

class Login(models.Model):


    def __str__(self):
        return self.id
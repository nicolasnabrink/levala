from django.db import models
from django.utils.html import escape, mark_safe
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    name = models.CharField(max_length=255)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    cpf = models.IntegerField(default=0)
    tel = models.IntegerField(default=0)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.name}'

class Company(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    logoURL = models.URLField(max_length=300, null=True, blank=True)
    cnpj = models.IntegerField(default=0)
    tel = models.IntegerField(default=0)
    job = models.CharField(max_length=255, default='Municipal')
    city = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.name}'
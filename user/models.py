from django.db import models
from django.utils.html import escape, mark_safe
from django.contrib.auth.models import AbstractUser
from django.db.models import Avg
from django.core.validators import MaxValueValidator, MinValueValidator

JOBS = [
    ('Municipal', 'Municipal'),
    ('Estadual', 'Estadual'),
    ('Nacional', 'Nacional'),
]

class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    cpf = models.IntegerField(default=0)
    tel = models.IntegerField(default=0)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

class Company(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    logoURL = models.URLField(max_length=300, null=True, blank=True)
    cnpj = models.IntegerField(default=0)
    tel = models.IntegerField(default=0)
    job = models.CharField(max_length=255, default='Municipal', choices=JOBS)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

class Admin(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

    def __str__(self):
        return f'{self.name}'

class Pedido(models.Model):
    user = models.ForeignKey(to=User, related_name='pedidos',on_delete=models.CASCADE)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.datetime}'

class Comment(models.Model):
    pedido = models.OneToOneField(Pedido, related_name='comments', on_delete = models.CASCADE, primary_key=True)
    review = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0, validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])

class Reply(models.Model):
    comment = models.OneToOneField(Comment, related_name='comments', on_delete = models.CASCADE, primary_key=True)
    text = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)

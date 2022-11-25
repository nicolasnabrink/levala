from django.db import models
from django.conf import settings

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} - {self.email}'

class Company(models.Model):
    cnpj = models.IntegerField(default=0)
    tel = models.IntegerField(default=0)
    job = models.CharField(max_length=255, default='Municipal')
    city = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0000)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user_id.name} from {self.city}'

class Client(models.Model):
    cpf = models.IntegerField(default=0)
    tel = models.IntegerField(default=0)
    city = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_id.name}'

class Admin(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_id.name}'

class Request(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    client_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.client_id.username} - {self.company_id.user_id.name} ({self.created_at})'


class Review(models.Model):
    rating = models.IntegerField(default=0)
    comment = models.CharField(max_length=255)
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE, default=000)

    def __str__(self):
        return f'{self.request_id.client_id.username} - {self.request_id.company_id.user_id.name} ({self.request_id.created_at}), {self.comment} ({self.rating})'
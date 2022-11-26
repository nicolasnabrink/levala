from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        CLIENT = "CLIENT", "Client"
        COMPANY = "COMPANY", "Company"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class ClientManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CLIENT)


class Client(User):

    base_role = User.Role.CLIENT

    client = ClientManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Clients"


@receiver(post_save, sender=Client)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CLIENT":
        ClientProfile.objects.create(user=instance)


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.IntegerField(default=0)
    tel = models.IntegerField(default=0)
    city = models.CharField(max_length=255)


class CompanyManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.COMPANY)


class Company(User):

    base_role = User.Role.COMPANY

    company = CompanyManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Companys"


class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    logoURL = models.URLField(max_length=300, null=True, blank=True)
    cnpj = models.IntegerField(default=0)
    tel = models.IntegerField(default=0)
    job = models.CharField(max_length=255, default='Municipal')
    city = models.CharField(max_length=255)
    score = models.IntegerField(blank=True)


@receiver(post_save, sender=Company)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "COMPANY":
        CompanyProfile.objects.create(user=instance)
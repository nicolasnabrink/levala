from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Company,Client

class ClientSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    cpf = forms.CharField(required=True)
    tel = forms.CharField(required=True)
    city = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.name = self.cleaned_data.get('name')
        user.save()
        client = Client.objects.create(user=user)
        client.tel=self.cleaned_data.get('tel')
        client.city=self.cleaned_data.get('city')
        client.cpf=self.cleaned_data.get('cpf')
        client.save()
        return user

class CompanySignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    logoURL = forms.CharField(required=True)
    cnpj = forms.CharField(required=True)
    tel = forms.CharField(required=True)
    job = forms.CharField(required=True)
    city = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.name = self.cleaned_data.get('name')
        user.save()
        company = Company.objects.create(user=user)
        company.tel=self.cleaned_data.get('tel')
        company.logoURL=self.cleaned_data.get('logoURL')
        company.cnpj=self.cleaned_data.get('cnpj')
        company.city=self.cleaned_data.get('city')
        company.job=self.cleaned_data.get('job')
        company.save()
        return user

class UpdateProfileForm(forms.ModelForm):
    name = forms.CharField(required=True)
    cpf = forms.CharField(required=True)
    tel = forms.CharField(required=True)
    city = forms.CharField(required=True)

    class Meta:
        model = Client
        fields = ['cpf', 'tel', 'city']
    @transaction.atomic
    def save(self, commit=True):
        user = super(ClientSignUpForm, self).save(commit=False)
        user.is_client = True
        user.name = self.cleaned_data.get('name')
        user.save()
        client.tel=self.cleaned_data.get('tel')
        client.city=self.cleaned_data.get('city')
        client.cpf=self.cleaned_data.get('cpf')
        client.save()

        return user

        
        
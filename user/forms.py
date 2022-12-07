from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Company,Client, Pedido, Comment, Reply

JOBS = [
    ('Municipal', 'Municipal'),
    ('Estadual', 'Estadual'),
    ('Nacional', 'Nacional'),
]

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
    job = forms.ChoiceField(required=True, choices=JOBS)
    city = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.save()
        company = Company.objects.create(user=user)
        company.name = self.cleaned_data.get('name')
        company.tel=self.cleaned_data.get('tel')
        company.logoURL=self.cleaned_data.get('logoURL')
        company.cnpj=self.cleaned_data.get('cnpj')
        company.city=self.cleaned_data.get('city')
        company.job=self.cleaned_data.get('job')
        company.save()
        return user

class UpdateClientProfileForm(forms.ModelForm):
    name = forms.CharField(required=True)
    cpf = forms.CharField(required=True)
    tel = forms.CharField(required=True)
    city = forms.CharField(required=True)

    class Meta:
        model = User
        fields = [ 'name','cpf', 'tel', 'city']

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        client = Client.objects.filter(user=user)
        client.name = self.cleaned_data.get('name')
        client.tel=self.cleaned_data.get('tel')
        client.city=self.cleaned_data.get('city')
        client.cpf=self.cleaned_data.get('cpf')

        return user

class UpdateCompanyProfileForm(forms.ModelForm):
    name = forms.CharField(required=True)
    logoURL = forms.CharField(required=True)
    cnpj = forms.CharField(required=True)
    tel = forms.CharField(required=True)
    job = forms.ChoiceField(required=True, choices=JOBS)
    city = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['name', 'cnpj', 'tel', 'job','city', 'logoURL']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.save()
        company = Company.objects.filter(user=user)
        company.name = self.cleaned_data.get('name')
        company.tel=self.cleaned_data.get('tel')
        company.logoURL=self.cleaned_data.get('logoURL')
        company.cnpj=self.cleaned_data.get('cnpj')
        company.city=self.cleaned_data.get('city')
        company.job=self.cleaned_data.get('job')
        return user

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('body',)

        labels = {
            'body': 'Conteudo'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('pedido','review','score',)

        labels = {
            'pedido':'Pedido',
            'review': 'Avaliacao',
            'score': 'Nota',
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('text',)

        labels = {
            'text':'Resposta',
        }
        
        
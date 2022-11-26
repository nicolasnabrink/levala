from django import forms
from user.models import Company, Client

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('username', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Nome', 'label': 'alo'}),
            'password': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Nome', 'label': 'alo'}),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('username', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Nome', 'label': 'alo'}),
            'password': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Nome', 'label': 'alo'}),
        }

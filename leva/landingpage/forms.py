from django import forms
from companies.models import Company, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Nome', 'label': 'alo'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Nome', 'label': 'alo'}),
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('logoURL', 'cnpj', 'tel', 'job', 'city', 'score')

        widgets = {
            'cnpj': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'cnpj', 'label': 'alo'}),
            'tel': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'tel', 'label': 'alo'}),
            'job': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'job', 'label': 'alo'}),
            'city': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'city', 'label': 'alo'}),
            'logoURL': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link de uma imagem associada à postagem'}),
        }
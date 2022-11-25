from django.shortcuts import render
from django.http import HttpResponse
from companies.models import Company, User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import UserForm, CompanyForm
from django.urls import reverse_lazy


def index(request):
    context = {}
    return render(request, 'landingpage/index.html', context)

class Cadastro_empresa(CreateView):
    model = User
    form_class = UserForm
    template_name = 'landingpage/cadastro_empresa.html'
    success_url = reverse_lazy('index')

class Dados_empresa(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'landingpage/dados_empresa.html'
    success_url = reverse_lazy('index')
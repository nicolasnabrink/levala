from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import ClientSignUpForm, CompanySignUpForm, UpdateClientProfileForm, UpdateCompanyProfileForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Client, Company 

def register(request):
    return render(request, 'user/register.html')

class customer_register(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'user/client_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class employee_register(CreateView):
    model = User
    form_class = CompanySignUpForm
    template_name = 'user/company_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'user/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('index')

def profile_client(request, user_id):
    client = get_object_or_404(Client, user_id=user_id)
    context = {'client': client}
    return render(request, 'user/profile.html', context)

class UpdateClientProfile(UpdateView):
    form_class = UpdateClientProfileForm
    template_name = 'user/update_client_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user.client

class UpdateCompanyProfile(UpdateView):
    form_class = UpdateCompanyProfileForm
    template_name = 'user/update_company_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user.company
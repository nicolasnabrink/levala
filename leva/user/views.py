from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from user.forms import ClientForm, CompanyForm
from django.contrib.auth.forms import UserCreationForm


def signup_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ClientForm()

    context = {'form': form}
    return render(request, 'signup.html', context)

def signup_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = CompanyForm()

    context = {'form': form}
    return render(request, 'signup.html', context)

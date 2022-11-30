from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import ClientSignUpForm, CompanySignUpForm, UpdateProfileForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Client

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

class UpdateProfile(UpdateView):
    form_class = UpdateProfileForm
    template_name = 'user/update_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user.client

    

        
    '''def update_profile(request, user_id):
        args = {}

        if request.method == 'POST':
            form = UpdateProfile(request.POST, instance=request.user)
            form.actual_user = request.user
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse(''))
        else:
            form = UpdateProfile()

        args['form'] = form
        return render(request, 'user/update_profile.html', args)'''

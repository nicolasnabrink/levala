from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from .forms import ClientSignUpForm, CompanySignUpForm, UpdateClientProfileForm, UpdateCompanyProfileForm, PedidoForm, CommentForm, ReplyForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Client, Company, Pedido, Comment, Reply
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='login')
def create_pedido(request, user_id):
    company = get_object_or_404(Company, pk=user_id)
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido_user = request.user
            pedido_body = form.cleaned_data['body']
            pedido = Pedido.objects.create(user=pedido_user,
                            body=pedido_body,
                            company=company)
            pedido.save()
            return HttpResponseRedirect(
                reverse('companies:detail', args=(user_id, )))
    else:
        form = PedidoForm()
    context = {'form': form, 'company': company}
    return render(request, 'companies/pedido.html', context)

def create_comment(request, companyuser_id):
    company = get_object_or_404(Company, pk=companyuser_id)
    user_id = request.user.id
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.fields["pedido"].queryset = Pedido.objects.filter(user_id=request.user, company_id=companyuser_id)
        if form.is_valid():
            comment_score = form.cleaned_data['score']
            comment_review = form.cleaned_data['review']
            comment_pedido = form.cleaned_data['pedido']
            comment = Comment.objects.create(score=comment_score,
                            review=comment_review,
                            pedido=comment_pedido)
            comment.save()
            return HttpResponseRedirect(
                reverse('companies:detail', args=(companyuser_id, )))
    else:
        form = CommentForm()
        form.fields["pedido"].queryset = Pedido.objects.filter(user_id=request.user, company_id=companyuser_id)
    context = {'form': form, 'company' : company,}
    return render(request, 'companies/comment.html', context)

def create_reply(request, comment_id):
    pedido = get_object_or_404(Pedido, pk=comment_id)
    company_id = pedido.company_id
    company = get_object_or_404(Company, pk=company_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply_text = form.cleaned_data['text']
            reply = Reply.objects.create(comment=comment,
                            text=reply_text,)
            reply.save()
            return HttpResponseRedirect(
                reverse('companies:detail', args=(company_id, )))
    else:
        form = ReplyForm()
    context = {'form': form, 'company': company, 'pedido': pedido, 'comment' : comment}
    return render(request, 'companies/reply.html', context)

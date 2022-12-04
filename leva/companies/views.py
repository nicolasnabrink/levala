from django.shortcuts import render
from django.http import HttpResponse
from user.models import Company, Pedido, Comment
from django.shortcuts import render, get_object_or_404

# Create your views here

def detail_company(request, user_id):
    company = get_object_or_404(Company, user_id=user_id)
    pedidos_list = Pedido.objects.filter(company_id=user_id)
    comments_list = Comment.objects.all()
    context = {'company': company, 'pedidos_list': pedidos_list, 'comments_list': comments_list, }
    return render(request, 'companies/detail.html', context)

def list_companies(request):
    company_list = Company.objects.all()
    city_list = Company.objects.order_by('city').values('city').distinct()
    context = {
        'company_list': company_list,
        'city_list': city_list,
    }
    return render(request, 'companies/list.html', context)

def is_valid_queryparam(param):
    return param != '' and param is not None

def search_companies(request):
    
    qs = Company.objects.all()
    name_query = request.GET.get('query_name')
    city_query = request.GET.get('query_city')
    job_query = request.GET.get('query_job')

    if is_valid_queryparam(name_query):
        qs = qs.filter(name__icontains=name_query)
    
    elif is_valid_queryparam(city_query) and city_query != 'Escolha...':
        qs = qs.filter(city__icontains=city_query)

    elif is_valid_queryparam(job_query) and job_query != 'Escolha...':
        qs = qs.filter(job__icontains=job_query)

    context = {
        'company_list': qs
    }

    return render(request, 'companies/search.html', context)

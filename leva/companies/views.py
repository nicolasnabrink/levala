from django.shortcuts import render
from django.http import HttpResponse
from .models import Company
from django.shortcuts import render, get_object_or_404

# Create your views here.
def detail_company(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    context = {'company': company}
    return render(request, 'companies/detail.html', context)

def list_companies(request):
    company_list = Company.objects.all()
    context = {'company_list': company_list}
    return render(request, 'companies/index.html', context)

def search_companies(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        company_list = Company.objects.filter(name__icontains=search_term)
        context = {"company_list": company_list}
    return render(request, 'companies/search.html', context)
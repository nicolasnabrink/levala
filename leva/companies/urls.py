from django.urls import path

from . import views

app_name = 'companies'
urlpatterns = [
    path('', views.list_companies, name='index'),
    path('search/', views.search_companies, name= 'search'),
    path('<int:company_id>/', views.detail_company, name='detail'),
]
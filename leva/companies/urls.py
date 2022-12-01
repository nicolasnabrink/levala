from django.urls import path
from .views import detail_company, list_companies,search_companies
from . import views

app_name = 'companies'
urlpatterns = [
    path('', views.list_companies, name='list'),
    path('search/', views.search_companies, name= 'search'),
    path('<int:user_id>/', views.detail_company, name='detail'),
]
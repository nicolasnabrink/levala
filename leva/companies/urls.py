from django.urls import path
from .views import detail_company, list_companies,search_companies
from . import views
from user import views as vs
from user.views import create_pedido, create_comment
from user.models import User

app_name = 'companies'
urlpatterns = [
    path('', views.list_companies, name='list'),
    path('search/', views.search_companies, name= 'search'),
    path('<int:user_id>/', views.detail_company, name='detail'),
    path('update_company_profile/<int:user_id>/',vs.UpdateCompanyProfile.as_view(), name='update_company_profile'),
    path('<int:user_id>/pedido/', vs.create_pedido, name='create_pedido'),
    path('<int:companyuser_id>/comment/', vs.create_comment, name='create_comment')
]


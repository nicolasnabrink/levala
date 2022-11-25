from django.urls import path
from . import views
from .views import Cadastro_empresa, Dados_empresa

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_empresa/', Cadastro_empresa.as_view(), name='cadastro_empresa'),
    path('dados_empresa/', Dados_empresa.as_view(), name='dados_empresa'),
]
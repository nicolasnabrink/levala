from django.urls import path

from . import views

urlpatterns = [
    # Add paths das páginas estáticas
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
]
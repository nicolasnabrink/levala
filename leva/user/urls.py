from django.urls import path

from . import views

urlpatterns = [
    path('signup_client/', views.signup_client, name='signup_client'),
    path('signup_company/', views.signup_company, name='signup_company')
]
from django.urls import path
from .views import CompanyList, CompanyDetail, CommentList, CommentDetail, PedidoDetail, PedidoList

urlpatterns = [
    path('companies/<int:pk>/', CompanyDetail.as_view()),
    path('companies/', CompanyList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    path('comments/', CommentList.as_view()),
    path('pedidos/<int:pk>/', PedidoDetail.as_view()),
    path('pedidos/', PedidoList.as_view()),
]

from django.urls import path
from .views import ProductList, ProductDetail

urlpatterns = [
    path('products/', ProductList.as_view(), name='product_list'),  # Для GET и POST запросов
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),  # Для GET запросов по id
]

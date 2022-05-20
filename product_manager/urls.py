from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProductsAPIView, OrderAPIView

urlpatterns = [
    path('products/', ProductsAPIView.as_view(), name='products'),
    path('products/<str:name>/', ProductsAPIView.as_view(), name='products_filtered_by_name'),
    path('orders/', OrderAPIView.as_view(), name='orders'),
]

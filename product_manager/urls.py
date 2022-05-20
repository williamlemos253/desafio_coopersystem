from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProductsAPIView

urlpatterns = [
    path('products/', ProductsAPIView.as_view(), name='products'),
]

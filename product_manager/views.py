from django.shortcuts import render
from . serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from .models import Product

# Create your views here.
class ProductsAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
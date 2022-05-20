from django.shortcuts import render
from . serializers import ProductSerializer, OrderSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from .models import Product, Order

# Create your views here.
class ProductsAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        if self.kwargs.get('name'):
            return self.queryset.filter(name=self.kwargs.get('name'))
        return self.queryset.all()

class OrderAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
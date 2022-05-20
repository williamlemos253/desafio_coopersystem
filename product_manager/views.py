from . serializers import ProductSerializer, OrderSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Product, Order
import django_filters.rest_framework


# Create your views here.
class ProductsAPIView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get_queryset(self):
        if self.kwargs.get('name'):
            return self.queryset.filter(name=self.kwargs.get('name'))
        return self.queryset.all()

class OrderAPIView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        if self.kwargs.get('status'):
            return self.queryset.filter(status=self.kwargs.get('status'))
        return self.queryset.all()

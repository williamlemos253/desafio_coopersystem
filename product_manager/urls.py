from django.urls import path
from .views import ProductsAPIView, OrderAPIView


urlpatterns = [
    path('products/', ProductsAPIView.as_view(), name='products'),
    path('product/<str:name>', ProductsAPIView.as_view(), name='products_filtered_by_name'),
    path('orders/', OrderAPIView.as_view(), name='orders'),
    path('order/<str:status>', OrderAPIView.as_view(), name='orders_filtered_by_status'),
]

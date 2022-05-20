from rest_framework import serializers

from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
    'status': {'read_only': True}
}
        model = Product
        fields = (
            'name',
            'price',
            'qtd',
            'status'
        )

class OrderSerializer
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

class OrderSerializer(serializers.ModelSerializer):
    
        class Meta:
            extra_kwargs = {
        'unit_price': {'read_only': True},
        'request_date': {'read_only': True},
        'total_price': {'read_only': True},
    }
            model = Order
            fields = (
                'product',
                'qtd',
                'unit_price',
                'total_price',
                'request_date',
                'requester',
                'postal_code',
                'uf',
                'City',
                'address',
                'Forwarding_agent',
                'status'
            )
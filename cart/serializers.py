from django.db.models import Sum
from rest_framework import serializers
from .models import Cart, CartItem
from main.models import Product

class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='product.title')
    price = serializers.ReadOnlyField(source='get_total_price')

    class Meta:
        model = CartItem
        fields = ('id', 'product', 'amount', 'price', )


class CartSerializer(serializers.ModelSerializer):
    products = CartItemSerializer(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Cart
        fields = ('user', 'products', )

    def to_representation(self, instance):
        representation = super(CartSerializer, self).to_representation(instance)
        representation['products'] = CartItemSerializer(instance.products.all(), many=True).data
        return representation




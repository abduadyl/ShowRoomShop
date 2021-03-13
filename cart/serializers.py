from rest_framework import serializers
from .models import Cart, CartItem


class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'cart_items',)


class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('amount', 'product_item',)
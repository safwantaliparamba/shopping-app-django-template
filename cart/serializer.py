from rest_framework import serializers

from .models import Cart,CartItem
from products.serializer import productSerializer
from users.serializer import CustomerSerializer



class CartItemSerializer(serializers.ModelSerializer):
    product = productSerializer()
    class Meta:
        model = CartItem
        fields = ('product',)
        
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    customer = CustomerSerializer()
    class Meta:
        model = Cart
        fields = ('id', 'items','customer')
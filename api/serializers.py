from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Order, Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'desc', 'cost', 'on_stock')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'quantity', 'product_id', 'username', 'total_price')

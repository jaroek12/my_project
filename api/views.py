from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import UserSerializer
from .models import Order, Product
from .serializers import OrderSerializer, ProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            user = self.get_object()
            user.delete()
            return Response('User deleted')
        else:
            return Response('Not allowed')

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            user = self.get_object()
            user.username = request.data['username']
            user.email = request.data['email']

            user.save()
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data)
        else:
            return Response('Not allowed')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        if username:
            orders = Order.objects.filter(username=username)
        else:
            orders = Order.objects.all()

        return orders

    def create(self, request, *args, **kwargs):
        product_id = request.data['product_id']
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response('Wrong product_id')
        else:
            quantity = request.data['quantity']
            if int(product.on_stock) - int(quantity) < 0:
                return Response('Insufficient quantity in stock')
            total_price = float(product.cost) * float(quantity)
            order = Order.objects.create(product_id=product_id, quantity=quantity,
                                         total_price=total_price, username=request.data['username'])

        product.on_stock = int(product.on_stock) - int(quantity)
        product.save()

        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        product_id = request.data['product_id']
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response('Wrong product_id')
        else:
            quantity = request.data['quantity']
            total_price = float(product.cost) * float(quantity)
            order = self.get_object()
            order.product_id = product_id
            order.quantity = quantity
            order.total_price = total_price
            order.username = request.data['username']

            order.save()

            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)

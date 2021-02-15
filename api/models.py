from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=32)
    desc = models.TextField(max_length=120)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    on_stock = models.IntegerField(default=50)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    product_id = models.PositiveSmallIntegerField()
    quantity = models.PositiveSmallIntegerField(default=1)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    username = models.CharField(max_length=16)

    def __str__(self):
        return f'Product ID: {self.product_id} ({str(self.quantity)})'

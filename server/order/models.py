from itertools import product
from statistics import quantiles
from django.db import models
from product.models import Product
from django.contrib.auth.models import User
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=100)
    place = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    stripe_token = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name = 'items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name = 'items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return str(self.id)
from django.contrib.auth import get_user_model
from django.db import models

from product.models import Product

User = get_user_model()

PROCESSING_CHOICES = (
    ('ORDERED', 'Ordered'),
    ('PROCESSING', 'Processing'),
    ('DELIVERED', 'Delivered')
)


class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.product.title} --> {self.order}'

class Order(models.Model):
    owner = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through=OrderItem)
    address = models.CharField(max_length=150)
    number = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices = PROCESSING_CHOICES)
    total_sum = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.owner}'



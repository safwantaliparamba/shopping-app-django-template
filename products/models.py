import uuid
from datetime import datetime

from django.db import models




class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4(),primary_key=True,unique=True,editable=False)
    name = models.CharField(max_length=225)
    image = models.FileField(upload_to='products/')
    small_description = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField(default=1)
    total_quantity = models.PositiveIntegerField(default=1)
    is_out_of_stock = models.BooleanField(default=False)
    added_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class Order(models.Model):
    PAYMENT_METHODS = (
        ('cash_on_delivery','Cash on Delivery'),
        ('online_payment','Online Payment'),
        ('upi_payment','UPI Payment')
    )

    product = models.ForeignKey(Product, related_name='orders',on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    customer = models.ForeignKey('users.Customer', related_name='orders',on_delete=models.CASCADE)
    address = models.TextField()
    payment_method = models.CharField(max_length=125, default='cash_on_delivery',choices=PAYMENT_METHODS)
    is_payed = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(auto_now_add=True)
    is_canceled = models.BooleanField(default=False)

    total_price = models.IntegerField(default=0,editable=False)

    def save(self, *args, **kwargs):
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'product - {self.product},customer - {self.customer}'

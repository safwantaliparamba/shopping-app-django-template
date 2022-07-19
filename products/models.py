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
from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    name = models.CharField(max_length=125)
    user = models.OneToOneField(User, related_name='customer',on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name
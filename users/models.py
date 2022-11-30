import uuid
from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    id = models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4())
    name = models.CharField(max_length=125)
    user = models.OneToOneField(User, related_name='customer',on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    pin_code = models.PositiveIntegerField(default=000000)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
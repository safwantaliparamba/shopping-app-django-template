from django.db import models



class Cart(models.Model):
    product = models.ForeignKey('products.Product', related_name='cart',on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    customer = models.ForeignKey('users.Customer', related_name='cart',on_delete=models.CASCADE)
    address = models.TextField()

    total_price = models.IntegerField(default=0,editable=False)

    def save(self, *args, **kwargs):
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'product - {self.product},customer - {self.customer}'

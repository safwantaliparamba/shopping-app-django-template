from django.db import models


class Cart(models.Model):
    total_price = models.IntegerField(default=0)
    customer = models.OneToOneField('users.Customer',related_name='cart',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.customer)


class CartItem(models.Model):
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey('products.Product',on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0)
    cart = models.ForeignKey(Cart,related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.total_price)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.product.price
        super().save(*args, **kwargs)
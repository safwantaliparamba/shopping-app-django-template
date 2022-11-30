from datetime import datetime

from django.db import models




class Product(models.Model):
    PRODUCT_CATEGORIES = (
        ('home_appliances','Home Appliances'),
        ('fashion','Fashion'),
        ('electronics','Electronics'),
        ('books','Books'),
        ('groceries','Groceries'),
        ('food_and_food_products','Food and Food Products'),
        ('jewelry','Jewelry'),
        ('toys','Toys'),
    )

    name = models.CharField(max_length=225)
    image = models.FileField(upload_to='products/')
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField(default=1)
    margin = models.PositiveIntegerField(default=1)
    total_price = models.PositiveBigIntegerField(default=1,editable=False)
    total_quantity = models.PositiveIntegerField(default=1)
    is_out_of_stock = models.BooleanField(default=False)
    added_date = models.DateTimeField(default=datetime.now)
    category = models.CharField(max_length=125,choices=PRODUCT_CATEGORIES)
    delivery_charge = models.PositiveIntegerField(default=40)
    discount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        self.total_price = self.price + self.margin
        super().save(*args, **kwargs)



class Order(models.Model):
    customer = models.OneToOneField('users.Customer', related_name='order',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.customer)

class OrderItem(models.Model):
    PAYMENT_METHODS = (
        ('cash_on_delivery','Cash on Delivery'),
        ('net_banking','Net Banking'),
        ('upi_payment','UPI Payment'),
        ('emi','EMI'),
    )
    STATUS = (
        ('booked','Booked'),
        ('shipped','Shipped'),
        ('out_for_delivery','Out for Delivery'),
        ('delivered','Delivered'),
        ('canceled','Canceled'),
    )

    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='orders',on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.TextField(null=True, blank=True)
    payment_method = models.CharField(max_length=125, default='cash_on_delivery',choices=PAYMENT_METHODS)
    is_payed = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(auto_now_add=True)
    is_canceled = models.BooleanField(default=False)
    total_price = models.IntegerField(default=0,editable=False)
    status = models.CharField(max_length=125,choices=STATUS,default='booked')
    shipped_date = models.DateTimeField(null=True, blank=True,editable=False)
    out_for_delivery_date = models.DateTimeField(null=True, blank=True,editable=False)
    delivered_date = models.DateTimeField(null=True, blank=True,editable=False)
    cancelled_date = models.DateTimeField(null=True, blank=True,editable=False)

    def save(self, *args, **kwargs):
        self.total_price = self.product.total_price * self.quantity
        self.address = self.order.customer.address
        if not self.status == 'delivered' and self.is_canceled :
            self.is_canceled = True
        if self.is_canceled:
            self.status = 'canceled'
        self.is_payed = True
        if self.payment_method == 'cash_on_delivery':
            self.is_payed == False
        if self.status == 'shipped':
            self.shipped_date = datetime.now()
        if self.status == 'out_for_delivery':
            self.out_for_delivery_date = datetime.now()
        if self.status == 'delivered':
            self.delivered_date = datetime.now()
        if self.status == 'canceled':
            self.cancelled_date = datetime.now()

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

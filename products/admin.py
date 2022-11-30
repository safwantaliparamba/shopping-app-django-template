from django.contrib import admin

from .models import Product,OrderItem,Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','image','id','short_description','total_price','total_quantity','is_out_of_stock']



class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order','product','quantity','payment_method','is_payed','ordered_date','status','total_price']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer']


admin.site.register(Product,ProductAdmin)
admin.site.register(OrderItem,OrderItemsAdmin)
admin.site.register(Order,OrderAdmin)

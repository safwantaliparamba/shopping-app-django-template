from django.contrib import admin

from .models import Product,Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','image','id','small_description','price','total_quantity','is_out_of_stock']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','customer','id','quantity','total_price','is_payed','ordered_date','is_payed']


admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)

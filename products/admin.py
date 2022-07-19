from django.contrib import admin

from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','image','id','small_description','price','total_quantity','is_out_of_stock']


admin.site.register(models.Product,ProductAdmin)

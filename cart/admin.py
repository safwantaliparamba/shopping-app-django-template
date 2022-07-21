from django.contrib import admin

from .models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ['product','id','quantity','customer','total_price']


admin.site.register(Cart,CartAdmin)
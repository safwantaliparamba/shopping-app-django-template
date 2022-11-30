from django.contrib import admin

from . import models


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'phone','created_at','is_admin','address']



admin.site.register(models.Customer,CustomerAdmin)
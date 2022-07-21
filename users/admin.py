from django.contrib import admin

from . import models


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'phone','is_admin','address']



admin.site.register(models.Customer,CustomerAdmin)
from django.contrib import admin
from .models import *

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'about', 'price']


@admin.register(KarzinkaModel)
class KarzinkaAdmin(admin.ModelAdmin):
    list_display = ['owner', 'product', 'count', 'created', 'completed']


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['owner', 'created', 'qabul_qiluvchi']






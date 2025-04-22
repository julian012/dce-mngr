from django.contrib import admin

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'is_available', 'product_stock', 'product_price')
    ordering = ('id',)

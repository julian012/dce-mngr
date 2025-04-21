from django.contrib import admin

from .models import (
    Buyout,
    BuyoutProduct
)

@admin.register(Buyout)
class BuyoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'total_price', 'buyout_date', 'type_payment_method', 'number_card')
    ordering = ('id',)

@admin.register(BuyoutProduct)
class BuyoutProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyout', 'product', 'quantity', 'product_price')
    ordering = ('id',)

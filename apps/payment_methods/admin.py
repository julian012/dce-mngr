from django.contrib import admin

from .models import PaymentMethod
@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_payment_method', 'number_card', 'date_card', 'cvv_card', 'owner')
    ordering = ('id',)

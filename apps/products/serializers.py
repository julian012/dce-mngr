from rest_framework import serializers

from .models import Product

class OnlyAvailableProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'image', 'product_stock', 'product_price', 'is_available')
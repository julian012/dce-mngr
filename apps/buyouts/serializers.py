from rest_framework import serializers
from .models import (
    Buyout,
    BuyoutProduct)

class HistoryProductSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()

    class Meta:
        model = BuyoutProduct
        fields = ('product_name', 'product_price', 'quantity')

    def get_product_name(self, obj: BuyoutProduct):
        return obj.product.name


class HistoryBuyoutSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Buyout
        fields = ('id', 'total_price', 'buyout_date', 'type_payment_method', 'number_card', 'products')

    def get_products(self, obj: Buyout):
        products = BuyoutProduct.objects.filter(buyout__id=obj.id)
        serializer = HistoryProductSerializer(instance=products, many=True)
        return serializer.data

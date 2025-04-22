from rest_framework import serializers
from django.forms.models import model_to_dict

from .models import ShoppingCart
from ..users.models import User
from ..products.models import Product
from ..products.serializers import OnlyAvailableProductSerializer


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ('id', 'user', 'product', 'quantity')

    def create(self, validated_data):
        print(self.context['request'])
        data = self.context['request']['data']
        validated_data['user'] = User.objects.get(id=data['user'])
        validated_data['product'] = Product.objects.get(id=data['product'])
        return super(ShoppingCartSerializer, self).create(validated_data)

class ActualShoppingCartUserSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    class Meta:
        model = ShoppingCart
        fields = ('product', 'quantity')

    def get_product(self, obj: ShoppingCart):
        serializer = OnlyAvailableProductSerializer(instance=obj.product, many=False)
        return serializer.data

from requests import Response
from django.db import transaction
from rest_framework.decorators import (
    api_view,
    permission_classes
)
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK
)

from .models import ShoppingCart
from .serializers import (
    ActualShoppingCartUserSerializer,
    ShoppingCartSerializer
)


@api_view(['GET'])
@permission_classes([])
def show_shopping_cart(request):
    products = ShoppingCart.objects.filter(user__id=1)
    serializer = ActualShoppingCartUserSerializer(instance=products, many=True)
    return Response(serializer.data, status=HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([])
def delete_from_shopping_cart(request, product_id):
    product = ShoppingCart.objects.get(user__id=1, product__id=product_id)
    product.delete()
    return Response({'deleted': 'OK'}, status=HTTP_200_OK)

@api_view(['POST'])
@permission_classes([])
@transaction.atomic
def add_product_shopping_cart(request):
    cart_data = { 'user': 1, 'product': request.data.get('product'), 'quantity': request.data.get('quantity') }
    serializer = ShoppingCartSerializer(data=cart_data, context={'request': { 'data': cart_data }})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=HTTP_200_OK)



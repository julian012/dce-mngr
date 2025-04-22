from requests import Response
from rest_framework.decorators import (
    api_view,
    permission_classes
)
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK
)

from apps.products.models import Product
from apps.products.serializers import OnlyAvailableProductSerializer


@api_view(['GET'])
@permission_classes([])
def show_available_products(request):
    products = Product.objects.filter(is_available=True, product_stock__gt=0)
    serializer = OnlyAvailableProductSerializer(instance=products, many=True)
    return Response(serializer.data, status=HTTP_200_OK)

# Create your views here.

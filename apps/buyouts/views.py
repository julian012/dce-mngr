from django.shortcuts import render
from rest_framework.decorators import (
    api_view,
    permission_classes
)
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK
)

from .serializers import HistoryBuyoutSerializer

from .models import Buyout

@api_view(['GET'])
@permission_classes([])
def show_user_history(request):
    orders = Buyout.objects.filter(buyer__id=1)
    serializer = HistoryBuyoutSerializer(instance=orders, many=True)
    return Response(serializer.data, status=HTTP_200_OK)

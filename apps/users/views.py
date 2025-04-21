from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.decorators import (
    api_view,
    permission_classes
)
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_204_NO_CONTENT
)

from dce_mngr.authentication import token_expire_handler

@api_view(['POST'])
@permission_classes([])
def login(request):
    user = authenticate(username=request.data.get('email', None), password=request.data.get('password', None))
    if user is None:
        return Response({'non_field_errors': ['No es posible iniciar sesion con las credenciales proveídas.']}, 400)
    user.save(update_fields=['last_connection'])
    token, created = Token.objects.get_or_create(user=user)
    if not created:
        is_expired, token = token_expire_handler(token)
    return Response({'auth_token': token.key}, HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    token = Token.objects.get(key=request.headers['Authorization'].split()[1])
    token.delete()
    return Response(status=HTTP_204_NO_CONTENT)
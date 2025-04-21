from djoser.serializers import UserCreateSerializer as UserDjoserSerializer

from .models import User

class UserCreateSerializer(UserDjoserSerializer):
    class Meta(UserDjoserSerializer.Meta):
        model = User
        fields = ('id', 'first_name', 'last_name', 'type_identification', 'identification')
        depth = 1
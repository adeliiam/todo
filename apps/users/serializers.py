from rest_framework import serializers
from apps.users.validators import validate_phone_number
from apps.users.models import NewUser


class UserSerializer(serializers.ModelSerializer):
    phone_number=serializers.CharField(validators=[validate_phone_number])
    class Meta:
        model=NewUser
        fields='__all__'
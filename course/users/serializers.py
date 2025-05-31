from rest_framework.serializers import ModelSerializer

from users.models import User


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "password", "tg_chat_id", "phone_number")


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("tg_chat_id", "phone_number", "avatar")
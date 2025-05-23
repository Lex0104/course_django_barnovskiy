from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserRegisterSerializer, UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny

from .models import Habit
from .paginators import HabitsPaginator
from .serializers import HabitSerializer
from users.permissions import IsOwner


class HabitCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """Переопределение метода для автоматической привязки владельца к создаваемому объекту."""
        habit = serializer.save()
        habit.user = self.request.user
        habit.periodicity_of_sending = habit.periodicity
        habit.save()


class HabitPublishedListAPIView(ListAPIView):
    queryset = Habit
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """Возвращает объекты владельца и публичные объекты."""
        return Habit.objects.filter(published=True)


class HabitUserListAPIView(ListAPIView):
    queryset = Habit
    serializer_class = HabitSerializer
    pagination_class = HabitsPaginator

    def get_queryset(self):
        """Возвращает список разрешений, требуемых для пользователей группы moderators."""
        user = self.request.user
        return Habit.objects.filter(user=user)


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit
    permission_classes = [IsOwner]

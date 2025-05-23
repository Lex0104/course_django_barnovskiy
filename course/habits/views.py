from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny

from habits.models import Habit
from habits.paginators import HabitsPaginator
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.periodicity_of_sending = habit.periodicity
        habit.save()


class HabitPublishedListAPIView(ListAPIView):
    queryset = Habit
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Habit.objects.filter(published=True)


class HabitUserListAPIView(ListAPIView):
    queryset = Habit
    serializer_class = HabitSerializer
    pagination_class = HabitsPaginator

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit
    permission_classes = [IsOwner]

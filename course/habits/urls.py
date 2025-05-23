from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitCreateAPIView,
    HabitDestroyAPIView,
    HabitPublishedListAPIView,
    HabitUpdateAPIView,
    HabitUserListAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("habits/create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("habits/published/", HabitPublishedListAPIView.as_view(), name="habits_published"),
    path("habits/user/", HabitUserListAPIView.as_view(), name="habits_user"),
    path("habits/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("habits/<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habit_delete"),
]
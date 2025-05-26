from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import FieldFillingValidator, RelatedHabitValidator


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        exclude = ("published",)
        validators = [
            RelatedHabitValidator("related_habit"),
            FieldFillingValidator("award", "related_habit", "nice_habit"),
        ]
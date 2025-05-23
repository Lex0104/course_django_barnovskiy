from datetime import timedelta

from rest_framework.exceptions import ValidationError


def execution_time_validator(value):
    if value:
        if value > timedelta(seconds=120):
            raise ValidationError("Продолжительность выполнения привычки не может быть более 120 секунд")


class RelatedHabitValidator:

    def __init__(self, related_habit):
        self.related_habit = related_habit

    def __call__(self, value):
        habit = value.get(self.related_habit)
        if habit:
            if not habit.nice_habit:
                raise ValidationError("Связанная привычка должна быть приятной")


class FieldFillingValidator:

    def __init__(self, award, related_habit, nice_habit):
        self.award = award
        self.related_habit = related_habit
        self.nice_habit = nice_habit

    def __call__(self, value):
        award_field = value.get(self.award)
        related_habit_field = value.get(self.related_habit)
        nice_habit_field = value.get(self.nice_habit)

        if award_field and related_habit_field:
            raise ValidationError("Может быть заполнено поле reward или поле related_habit")
        if nice_habit_field:
            if award_field or related_habit_field:
                raise ValidationError("У приятной привычки не может быть связанной привычки или вознаграждения")
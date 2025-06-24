from datetime import timedelta

from django.core.validators import MaxValueValidator
from django.db import models

from habits.validators import execution_time_validator
from users.models import User


class Habit(models.Model):
    """Модель Habit для хранения информации о привычках пользователей."""
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name="Автор привычки", related_name="habit", null=True
    )
    place = models.CharField(max_length=150, verbose_name="Место выполнения привычки", blank=True, null=True)
    time = models.DateTimeField(verbose_name="Время выполнения привычки", blank=True, null=True)
    action = models.CharField(max_length=250, verbose_name="Привычка")
    nice_habit = models.BooleanField(verbose_name="Показатель приятной привычки", default=False)
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Приятная привычка",
        blank=True,
        null=True,
        related_name="habit",
    )
    periodicity = models.PositiveIntegerField(
        validators=[MaxValueValidator(7)], verbose_name="Периодичность привычки", default=1
    )
    award = models.CharField(max_length=250, verbose_name="Вознаграждение", blank=True, null=True)
    execution_time = models.DurationField(
        validators=[execution_time_validator],
        verbose_name="Продолжительность выполнения привычки",
        default=timedelta(seconds=120),
    )
    published = models.BooleanField(verbose_name="Признак публичности", default=False)
    periodicity_of_sending = models.PositiveIntegerField(
        validators=[MaxValueValidator(7)], verbose_name="Периодичность отправки уведомления", default=1
    )

    class Meta:
        verbose_name = ("Привычка",)
        verbose_name_plural = "Привычки"
        ordering = ["id"]

    def __str__(self):
        return f"{self.action} - {self.nice_habit}"

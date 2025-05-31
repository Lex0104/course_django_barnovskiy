from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_message_for_user():
    """Функция отправки уведомления о повторении дел в Telegram."""
    habits = Habit.objects.filter(nice_habit=False)
    for habit in habits:
        habit.periodicity_of_sending -= 1
        if habit.periodicity_of_sending == 0:
            if habit.user.tg_chat_id:
                message = f"Уведомление! Сегодня необходимо {habit.action} в {habit.time} в {habit.place}!"
                send_telegram_message(chat_id=habit.user.tg_chat_id, message=message)
                habit.periodicity_of_sending = habit.periodicity
        habit.save()
import requests

from config import settings


def send_telegram_message(chat_id, message):
    """Отправка сообщения в телеграмм чат
        :param chat_id: id чата
        :param message: текст сообщения
        """
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    requests.get(f"{settings.TG_URL}{settings.TG_TOKEN}/sendMessage", params=params)
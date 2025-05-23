from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = PhoneNumberField(verbose_name="Номер телефона", blank=True, null=True)
    avatar = models.ImageField(upload_to="users/images", verbose_name="Аватар", blank=True, null=True)
    tg_chat_id = models.PositiveIntegerField(verbose_name="ID чата в  Telegram", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.email}"
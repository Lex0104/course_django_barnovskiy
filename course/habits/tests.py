from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="fortrst@example.com")
        self.habit = Habit.objects.create(user=self.user, action="Test", published=True)
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        url = reverse("habits:habit_create")
        data = {"action": "Test Create"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habit_published(self):
        url = reverse("habits:habits_published")
        response = self.client.get(url)
        data = response.json()
        result = [
            {
                "action": self.habit.action,
                "award": self.habit.award,
                "execution_time": "00:02:00",
                "id": self.habit.pk,
                "nice_habit": self.habit.nice_habit,
                "periodicity": 1,
                "periodicity_of_sending": 1,
                "place": self.habit.place,
                "related_habit": self.habit.related_habit,
                "time": self.habit.time,
                "user": self.user.pk,
            }
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_user(self):
        url = reverse("habits:habits_user")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "place": self.habit.place,
                    "time": self.habit.time,
                    "action": self.habit.action,
                    "nice_habit": self.habit.nice_habit,
                    "periodicity": self.habit.periodicity,
                    "award": self.habit.award,
                    "execution_time": "00:02:00",
                    "periodicity_of_sending": self.habit.periodicity_of_sending,
                    "user": self.user.pk,
                    "related_habit": self.habit.related_habit,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_update(self):
        url = reverse("habits:habit_update", args=(self.habit.pk,))
        data = {"action": "Test Update"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), "Test Update")

    def test_habit_delete(self):
        url = reverse("habits:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from habits.models import Habits
from users.models import CustomUser


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email="ssofstep7627@ya.ru")
        self.habit = Habits.objects.create(
            user=self.user,
            place="Дома",
            time="2023-13-05T14:31:00+03:00",
            action="Подтянуться 10 раз",
            nice_habit="False",
            periodicity=1,
            reward="Null",
            complete_time="00:02:00",
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        self.assertEqual(Habits.objects.all().count(), 1)

    def test_habit_retrieve(self):
        url = reverse("habits:retrieve_habits", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("periodicity"), self.habit.periodicity)

    def test_habit_list(self):
        url = reverse("habits:habits")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_update(self):
        url = reverse("habits:update_habits", args=(self.habit.pk,))
        data = {
            "place": "Во дворе дома",
            "time": "2024-12-05T16:32:00+03:00",
            "action": "Сделать 5 упражнений>",
            "is_nice": "True",
            "periodicity": 1,
            "complete_time": "00:02:00",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), "Во дворе дома")

    def test_habit_delete(self):
        url = reverse("habits:delete_habits", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habits.objects.all().count(), 0)

    def test_habit_public_list(self):
        url = reverse("habits:public_habits")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
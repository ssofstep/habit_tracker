from rest_framework.test import APITestCase

from users.models import CustomUser


class UserTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email='ssofstep7627@ya.ru', password='7627')

    def test_user_create(self):
        self.assertEqual(CustomUser.objects.all().count(), 1)

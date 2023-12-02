from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest (TestCase):
    def setup(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(
            username='testaccount',
            password='testpass'
        )
        self.pasta = Menu.objects.create(title='pasta', price=12, inventory=100)

    def loginTestUser(self) -> None:
        self.client.login(username='testaccount', password='testpass')

    def test_getall(self):
        self.loginTestUser()
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)

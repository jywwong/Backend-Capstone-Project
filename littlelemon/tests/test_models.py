from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_menu(self):
        item = Menu.objects.create(
            title='Hot Dog',
            price=5,
            inventory=100)

        self.assertEqual(item.title, 'Hot Dog')

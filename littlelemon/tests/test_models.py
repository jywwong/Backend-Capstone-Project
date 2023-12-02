from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_menu(self):
        item = Menu.objects.create(
            title='pasta',
            price=5,
            inventory=100)

        self.assertEqual(item.title, 'pasta')
        self.assertEqual(item.price, 12)
        self.assertEqual(item.inventory, 100)

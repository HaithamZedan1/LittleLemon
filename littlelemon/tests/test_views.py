from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pizza", price=10.99, inventory=20)
        Menu.objects.create(title="Pasta", price=8.99, inventory=15)
        Menu.objects.create(title="Salad", price=6.99, inventory=10)

    def test_getall(self):
        menus = Menu.objects.all()
        self.assertEqual(menus.count(), 3)

        self.assertEqual(menus[0].title, "Pizza")
        self.assertEqual(menus[1].title, "Pasta")
        self.assertEqual(menus[2].title, "Salad")
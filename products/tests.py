from django.test import TestCase

from products.models import Coffee, Food


class CoffeeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.coffee = Coffee.objects.create(
            name="TestCoffee",
            volume=150,
            cost=150,
            image=None 
        )
    
    def test_as_dict(self):
        self.assertEqual(self.coffee.as_dict, {
            "id": self.coffee.pk,
            "name": "TestCoffee",
            "volume": 150,
            "cost": 150,
        })
   
    def test_mixins_as_dict(self):
        self.assertEqual(self.coffee.mixins_as_dict, {
            "milk": False,
            "cinnamon": False,
            "syrup": False
        })
    
    def test_set_mixin(self):
        self.coffee.set_mixin(True, True, True)
        self.assertEqual(self.coffee.mixins_as_dict, {
            "milk": True,
            "cinnamon": True,
            "syrup": True
        }) 


class FoodModeltest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.food = Food.objects.create(
            name="TestFood",
            cost=150
        )
    
    def test_as_dict(self):
        self.assertEqual(self.food.as_dict, {
            "id": self.food.pk,
            "name": self.food.name,
            "cost": self.food.cost
        })

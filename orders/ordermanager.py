from django.http import HttpRequest
from django.conf import settings

from products.models import Coffee, Food


class OrderManager:
    def __init__(self, request: HttpRequest) -> None:
        self.session = request.session

        user_order = self.session.get(settings.ORDER_SESSION_ID)
        if not user_order:
            self.session[settings.ORDER_SESSION_ID] = {}
            user_order = self.session[settings.ORDER_SESSION_ID]
            user_order["order_food"] = []
            user_order["order_coffee"] = []
            self.session.modified = True
        
        self.user_order = user_order
        self.coffee: list[Coffee] = self.user_order["order_coffee"]
        self.food: list[Food] = self.user_order["order_food"]

    def add_coffee(self, coffee: Coffee):
        self.coffee.append(coffee.as_dict)
        self.session.modified = True

    def add_food(self, food: Food):
        self.food.append(food.as_dict)
        self.session.modified = True

    def remove_coffee(self, coffee: Coffee):
        if coffee.as_dict in self.coffee:
            self.coffee.remove(coffee.as_dict)
            self.session.modified = True
            return coffee

    def remove_food(self, food: Food):
        if food.as_dict in self.food:
            self.food.remove(food.as_dict)
            self.session.modified = True
            return food
   
    def get_coffies_models(self) -> list[Coffee]:
        r = []
        for coffee_dt in self.coffee:
            print(coffee_dt["id"])
            r.append(Coffee.objects.get(id=coffee_dt["id"]))
        for j in r:
            print(j.volume)
        return r 
    
    def get_total_price(self):
        return sum(food["cost"] for food in self.food) + sum(coffee["cost"] for coffee in self.coffee)

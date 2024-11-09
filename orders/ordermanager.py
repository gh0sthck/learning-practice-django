from decimal import Decimal
from django.http import HttpRequest
from django.conf import settings

from products.models import Coffee, Food


class OrderManager:
    """
    OrderManager class to manage currently user order. Manager use session method and current order
    will be "Set to none" if user logout from own account and not confirm order.
    ```
    >>> manager = OrderManager(request)
    >>> manager.add_coffee(coffee)
    >>> Coffee(...)
    ```
    """
    def __init__(self, request: HttpRequest) -> None:
        self.session = request.session
        self.user_bonus: Decimal = request.user.bonus

        user_order = self.session.get(settings.ORDER_SESSION_ID)
        if not user_order:
            self.session[settings.ORDER_SESSION_ID] = {}
            user_order = self.session[settings.ORDER_SESSION_ID]
            user_order["order_food"] = []
            user_order["order_coffee"] = []
            self.session.modified = True

        self.user_order = user_order
        self.coffee: list[dict] = self.user_order["order_coffee"]
        self.food: list[dict] = self.user_order["order_food"]

    def add_coffee(self, coffee: Coffee) -> Coffee:
        self.coffee.append(coffee.as_dict)
        self.session.modified = True
        return coffee

    def add_food(self, food: Food) -> Food:
        self.food.append(food.as_dict)
        self.session.modified = True
        return food

    def remove_coffee(self, coffee: Coffee) -> Coffee | None:
        if coffee.as_dict in self.coffee:
            self.coffee.remove(coffee.as_dict)
            self.session.modified = True
            return coffee

    def remove_food(self, food: Food) -> Food | None:
        if food.as_dict in self.food:
            self.food.remove(food.as_dict)
            self.session.modified = True
            return food

    def get_coffies_models(self) -> list[Coffee]:
        r = []
        for coffee_dt in self.coffee:
            r.append(Coffee.objects.get(id=coffee_dt["id"]))
        return r

    def get_total_price(self) -> int:
        total = sum(food["cost"] for food in self.food) + sum(
            coffee["cost"] for coffee in self.coffee
        )
        if total > 180:
            return int(total - self.user_bonus * total)
        return total 

from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from orders.ordermanager import OrderManager

from products.models import Coffee, Food
from products.forms import AddMixinForm


class CurrentOrder(View):
    mixin_form = AddMixinForm

    def get(self, request: HttpRequest):
        order_manager = OrderManager(request=request)
        order = order_manager
        forms = [
            self.mixin_form(coffee.mixins_as_dict)
            for coffee in order_manager.get_coffies_models()
        ]
        coffies = zip(order.coffee, forms)

        return render(
            request,
            "orders_order.html",
            {"order": order, "coffies": coffies, "foods": order_manager.food},
        )

    def post(self, request: HttpRequest):
        form = self.mixin_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            coffee_id = int(request.POST["id"])
            coffee = Coffee.objects.get(id=coffee_id)
            coffee.set_mixin(cd.get("cinnamon"), cd.get("milk"), cd.get("syrup"))
            coffee.save()
        return redirect("current_order")


class AddOrderCoffee(View):
    def post(self, request: HttpRequest, coffee_name: str):
        volume = int(self.request.POST["coffee_volume"])
        order_manager = OrderManager(request=request)
        coffee = Coffee.objects.filter(name=coffee_name, volume=volume)[0]
        order_manager.add_coffee(coffee)
        return redirect("main")


class AddOrderFood(View):
    def post(self, request: HttpRequest, food_id: int):
        food = Food.objects.get(id=food_id)
        order_manager = OrderManager(request)
        order_manager.add_food(food)
        return redirect("main")


class DelOrderCoffee(View):
    def post(self, request: HttpRequest, coffee_id: int):
        coffee = Coffee.objects.get(id=coffee_id)
        order_manager = OrderManager(request)
        order_manager.remove_coffee(coffee)
        return redirect("current_order")


class DelOrderFood(View):
    def post(self, request: HttpRequest, food_id: int):
        food = Food.objects.get(id=food_id)
        order_manager = OrderManager(request)
        order_manager.remove_food(food)
        return redirect("current_order")

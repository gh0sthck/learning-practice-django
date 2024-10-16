from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from orders.models import Order
from orders.utils import get_order
from products.models import Coffee, Food
from orders.forms import AddMixinForm


class CurrentOrder(View):
    def get(self, request: HttpRequest):
        user = request.user
        order = None
        mixin_form = AddMixinForm()

        if request.user.is_authenticated:
            order = get_order(user=user)
            if not order:
                order = Order.objects.create(user=user)
                order.save()

        return render(
            request, "orders_order.html", {"order": order, "mixin_form": mixin_form}
        )


class AddOrderCoffee(View):
    def post(self, request: HttpRequest, coffee_id: int):
        user = request.user
        order = get_order(user=user)
        coffee = Coffee.objects.get(id=coffee_id)

        if order:
            order.coffee = coffee
            order.save()
        else:
            new_order = Order.objects.create(coffee=coffee, user=user)
            new_order.save()

        return redirect("main")


class AddOrderFood(View):
    def post(self, request: HttpRequest, food_id: int):
        user = request.user
        order = get_order(user=user)
        food = Food.objects.get(id=food_id)

        if order:
            order.food = food
            order.save()
        return redirect("main")


class DelOrderCoffee(View):
    def post(self, request: HttpRequest, coffee_id: int):
        user = request.user
        order = get_order(user=user)
        coffee = Coffee.objects.get(id=coffee_id)
        if order.coffee == coffee:
            order.coffee = None
            order.save()
        return redirect("main")


class DelOrderFood(View):
    def post(self, request: HttpRequest, food_id: int):
        user = request.user
        order = get_order(user=user)
        food = Food.objects.get(id=food_id)
        if order.food == food:
            order.food = None
            order.save()
        return redirect("main")

from decimal import Decimal
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from orders.models import Mixin, Order
from orders.utils import get_mixin, get_order
from products.models import Coffee, Food
from orders.forms import AddMixinForm


class CurrentOrder(View):
    mixin_form = AddMixinForm

    def get(self, request: HttpRequest):
        user = request.user
        order = None
        mixin = None
        form = None

        if request.user.is_authenticated:
            order = get_order(user=user)
            if not order:
                order = Order.objects.create(user=user)
                order.save()
            mixin = get_mixin(order=order)
            if not mixin:
                mixin = Mixin.objects.create(order=order)
                mixin.save()
            form = self.mixin_form(mixin.as_dict)
        else:
            form = self.mixin_form()

        return render(
            request,
            "orders_order.html",
            {"order": order, "mixin_form": form},
        )

    def post(self, request: HttpRequest):
        form = self.mixin_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            mx = Mixin.objects.get(order=get_order(user=request.user))
            mx.set_mixin(cd.get("cinnamon"), cd.get("milk"), cd.get("syrup"))
            mx.save()
        return redirect("current_order")


class AddOrderCoffee(View):
    def post(self, request: HttpRequest, coffee_name: str):
        volume = int(self.request.POST["coffee_volume"])
        user = request.user
        order = get_order(user=user)
        coffee = Coffee.objects.filter(name=coffee_name, volume=volume)[0]

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

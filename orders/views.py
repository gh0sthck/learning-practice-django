from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View


from orders.models import Order
from products.models import Coffee, Food


class AddOrderCoffee(View):
    def post(self, request: HttpRequest, coffee_id: int):
        user = request.user
        try:
            order = Order.objects.get(user=user.id)
        except Order.DoesNotExist:
            order = None
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
        order = Order.objects.get(user=user.id)
        food = Food.objects.get(id=food_id)
        if order:
            order.food = food
            order.save()
        return redirect("main")


class DelOrderCoffee(View):
    def post(self, request: HttpRequest, coffee_id: int):
        user = request.user

        return redirect("main")

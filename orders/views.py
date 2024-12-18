from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from aogiri.redis_conn import get_redis_connection
from orders.ordermanager import OrderManager

from orders.utils import add_order, get_order
from products.models import Coffee, Food
from products.forms import AddMixinForm
from users.models import CoffeeUser


class CurrentOrder(View):
    mixin_form = AddMixinForm

    def get(self, request: HttpRequest):
        order_manager = OrderManager(request=request)
        forms = [
            self.mixin_form(coffee.mixins_as_dict)
            for coffee in order_manager.get_coffies_models()
        ]
        coffies = zip(order_manager.coffee, forms)

        confirmed_order = get_order(request.user.username)
        if confirmed_order:
            confirmed_order["coffies"] = [
                Coffee.objects.get(id=int(cid)) for cid in confirmed_order["coffies"]
            ]
            confirmed_order["food"] = [
                Food.objects.get(id=int(fid)) for fid in confirmed_order["food"]
            ]

        return render(
            request,
            "orders_order.html",
            {
                "order": order_manager,
                "coffies": tuple(coffies),
                "foods": order_manager.food,
                "confirmed_order": confirmed_order,
            },
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


class ConfirmOrder(View):
    def post(self, request: HttpRequest):
        post_data = dict(request.POST.lists())
        total_price = int(post_data["total_price"][0])
        coffee_ids = []
        food_ids = []
        current_user_balance: float = float(request.user.balance)

        if current_user_balance >= total_price:
            u = CoffeeUser.objects.get(id=request.user.id)
            u.pay_order(total_price)
            u.save()

            if post_data.get("coffee"):
                coffee_ids = list(map(int, post_data["coffee"]))
            if post_data.get("food"):
                food_ids = list(map(int, post_data["food"]))

            user_id = int(request.user.id)

            order = {
                "coffies": coffee_ids,
                "food": food_ids,
                "ready": False,
                "paid": True,
                "total_price": total_price,
            }
            request.session["user_order"] = {}
            add_order(user_id=user_id, order=order)

            return redirect("current_order")
        else:
            messages.add_message(
                request, messages.ERROR, "Недостаточно средств на балансе"
            )
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


class BaristaQueue(View):
    def get(self, request: HttpRequest):
        rc = get_redis_connection()

        queue: list[dict] = [
            (get_order(u.decode()))
            for u in rc.keys()
            if not u.decode().startswith("_") and not u.decode().startswith("celery")
        ]
        for order in queue:
            order["coffies"] = [
                Coffee.objects.get(id=int(cid)) for cid in order["coffies"]
            ]
            order["food"] = [Food.objects.get(id=int(fid)) for fid in order["food"]]

        return render(
            request, "orders_barista.html", {"queue": queue, "raw_queue": queue}
        )

    def post(self, request: HttpRequest):
        order = get_order(request.POST["ready_username"])
        order["ready"] = True
        rc = get_redis_connection()
        rc.set(name=request.POST["ready_username"], value=str(order))
        return redirect("barista_queue")


class CreateNewOrder(View):
    def post(self, request: HttpRequest):
        rc = get_redis_connection()
        rc.delete(request.user.username)
        return redirect("main")

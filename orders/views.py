from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.decorators import login_required

from orders.models import Order
from products.models import Coffee, Food


@login_required
class UpdateOrder(View):
    def post(self, request: HttpRequest, id: int):
        user = request.user
        order = Order.objects.filter(user_id=user.id)
        coffee = Coffee.objects.get(id=id)
        print(order)
        if order:
            order[0].coffe_id = coffee
            order[0].save()
        else:
            new_order = Order.objects.create(coffe_id=coffee, user_id=user)
            new_order.save()
        return redirect("main")

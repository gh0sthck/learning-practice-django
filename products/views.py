from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView

from orders.models import Order
from products.models import Coffee, Food


class AllCoffee(ListView):
    model = Coffee
    template_name = "coffee_all.html"
    context_object_name = "coffies"


class AllFood(ListView):
    model = Food
    template_name = "food_all.html"
    context_object_name = "foods"


class MainPage(View):
    def get(self, request):
        coffies = Coffee.objects.all()[:6]
        foods = Food.objects.all()[:6]
        order = Order.objects.all()
        user_order = Order.objects.get(user=request.user)

        ctx = {
            "foods": foods,
            "coffies": coffies,
            "ord": order,
            "current_order": user_order,
        }
        return render(request, template_name="main_page.html", context=ctx)

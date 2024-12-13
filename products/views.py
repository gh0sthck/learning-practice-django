from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator

from orders.ordermanager import OrderManager
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
        coffies = Coffee.objects.all()
        foods = Food.objects.all()

        coffies_vols: dict[Coffee, list[int]] = {}
        for coffee in coffies:
            if coffee.name not in coffies_vols:
                coffies_vols[coffee.name] = {coffee.volume: coffee.cost}
            else:
                coffies_vols[coffee.name].update({coffee.volume: coffee.cost})

        coffies = [Coffee.objects.filter(name=cof)[0] for cof in coffies_vols]

        coffee_paginator = Paginator(coffies, 4)
        food_paginator = Paginator(foods, 4)

        page_number = request.GET.get("page")
        page_obj_cof = coffee_paginator.get_page(page_number)
        page_obj_food = food_paginator.get_page(page_number)

        order_manager = OrderManager(request)
        user_order = order_manager.user_order

        ctx = {
            "foods": foods,
            "coffies": coffies,
            "current_order": user_order,
            "fd_page": page_obj_food,
            "cof_page": page_obj_cof,
            "cof_vols": coffies_vols,
        }
        return render(request, template_name="main_page.html", context=ctx)


class AddCoffee(CreateView):
    model = Coffee
    fields = ["name", "image", "cost", "volume"]
    template_name = "product_add.html"
    success_url = reverse_lazy("main")


class AddFood(CreateView):
    model = Food
    fields = ["name", "image", "cost"]
    template_name = "product_add.html"
    success_url = reverse_lazy("main")

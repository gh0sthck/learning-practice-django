from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator

from orders.models import Order
from orders.utils import get_order
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
        user_order = None
        coffee_paginator = Paginator(coffies, 4)
        food_paginator = Paginator(foods, 4)

        page_number = request.GET.get("page")
        page_obj_cof = coffee_paginator.get_page(page_number)
        page_obj_food = food_paginator.get_page(page_number)

        if request.user.is_authenticated:
            user_order = get_order(user=request.user)

        ctx = {
            "foods": foods,
            "coffies": coffies,
            "current_order": user_order,
            "fd_page": page_obj_food,
            "cof_page": page_obj_cof,
        }
        return render(request, template_name="main_page.html", context=ctx)


class AddCoffee(CreateView):
    model = Coffee
    fields = ["name", "cost", "volume"]
    template_name = "product_add.html"
    success_url = reverse_lazy("main")


class AddFood(CreateView):
    model = Food
    fields = ["name", "cost"]
    template_name = "product_add.html"
    success_url = reverse_lazy("main")

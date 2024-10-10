from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

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
        ord = Order.objects.all()
        ctx = {"foods": foods, "coffies": coffies, "ord": ord}
        return render(request, template_name="main_page.html", context=ctx)

    # @login_required
    def post(self, request: HttpRequest):
        print("post", request.POST)
        user = request.user
        # order = Order.objects.filter(user_id=user.id)

        print(request.POST)
        print(request.session.items())

        return render(request, template_name="main_page.html")

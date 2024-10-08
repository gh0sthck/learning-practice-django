from django.views.generic.list import ListView

from products.models import Coffee


class AllCoffee(ListView):
    model = Coffee
    template_name = "coffee_all.html"
    context_object_name = "coffies"

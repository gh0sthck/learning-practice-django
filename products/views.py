from django.views.generic.list import ListView

from products.models import Coffee


class AllCoffee(ListView):
    model = Coffee
    template_name = "products_all.html"

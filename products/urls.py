from django.urls import path

from products.views import AllCoffee

urlpatterns = [path("all_coffee", AllCoffee.as_view(), name="all_coffee")]

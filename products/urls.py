from django.urls import path

from products.views import AllCoffee, AllFood, MainPage, AddCoffee, AddFood

urlpatterns = [
    path("", MainPage.as_view(), name="main"),
    path("all_coffee", AllCoffee.as_view(), name="all_coffee"),
    path("all_food", AllFood.as_view(), name="all_food"),
    path("add_coffee", AddCoffee.as_view(), name="add_coffee"),
    path("add_food", AddFood.as_view(), name="add_food"),
]

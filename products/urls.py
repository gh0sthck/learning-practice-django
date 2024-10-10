from django.urls import path

from products.views import AllCoffee, AllFood, MainPage

urlpatterns = [
    path("", MainPage.as_view(), name="main"),
    path("all_coffee", AllCoffee.as_view(), name="all_coffee"),
    path("all_food", AllFood.as_view(), name="all_food"),
]

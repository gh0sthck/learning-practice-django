from django.urls import path

from orders.views import (
    AddOrderCoffee,
    AddOrderFood,
    CurrentOrder,
    DelOrderCoffee,
    DelOrderFood,
)


urlpatterns = [
    path(
        "add_order_coffee/<int:coffee_id>",
        AddOrderCoffee.as_view(),
        name="add_order_coffee",
    ),
    path(
        "add_order_food/<int:food_id>",
        AddOrderFood.as_view(),
        name="add_order_food",
    ),
    path(
        "del_order_coffee/<int:coffee_id>",
        DelOrderCoffee.as_view(),
        name="del_order_coffee",
    ),
    path(
        "del_order_food/<int:food_id>",
        DelOrderFood.as_view(),
        name="del_order_food",
    ),
    path("current", CurrentOrder.as_view(), name="current_order"),
]

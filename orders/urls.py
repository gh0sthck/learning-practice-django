from django.urls import path

from orders.views import (
    AddOrderCoffee,
    AddOrderFood,
    CurrentOrder,
    DelOrderCoffee,
    DelOrderFood,
    ConfirmOrder,
    BaristaQueue,
    CreateNewOrder,
)


urlpatterns = [
    path(
        "add_order_coffee/<str:coffee_name>",
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
    path("current/", CurrentOrder.as_view(), name="current_order"),
    path(
        "confirm_order",
        ConfirmOrder.as_view(),
        name="confirm_order",
    ),
    path(
        "queue/",
        BaristaQueue.as_view(),
        name="barista_queue",
    ),
    path(
        "new_order/",
        CreateNewOrder.as_view(),
        name="create_new_order"
    )
]

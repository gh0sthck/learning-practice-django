from django.urls import path

from orders.views import UpdateOrderCoffee, UpdateOrderFood


urlpatterns = [
    path(
        "update_order_coffee/<int:coffee_id>",
        UpdateOrderCoffee.as_view(),
        name="update_order_coffee",
    ),
    path(
        "update_order_food/<int:food_id>",
        UpdateOrderFood.as_view(),
        name="update_order_food",
    ),
]

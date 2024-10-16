from django.urls import path

from orders.views import AddOrderCoffee, AddOrderFood


urlpatterns = [
    path(
        "update_order_coffee/<int:coffee_id>",
        AddOrderCoffee.as_view(),
        name="add_order_coffee",
    ),
    path(
        "update_order_food/<int:food_id>",
        AddOrderFood.as_view(),
        name="add_order_food",
    ),
]

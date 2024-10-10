from django.urls import path

from orders.views import UpdateOrder


urlpatterns = [
    path("update_order/<int:id>", UpdateOrder.as_view(), name="update_order")
]

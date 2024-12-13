from django.http import HttpRequest
from .ordermanager import OrderManager


def order_manager(request: HttpRequest):
    return {"manager": OrderManager(request)}

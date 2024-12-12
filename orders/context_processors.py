from .ordermanager import OrderManager


def order_manager(request):
    return {"manager": OrderManager(request)}

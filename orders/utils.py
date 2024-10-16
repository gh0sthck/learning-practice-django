from typing import Optional

from orders.models import Order
from users.models import CoffeeUser


def get_order(user: CoffeeUser) -> Optional[Order]:
    order = None
    try:
        order = Order.objects.get(user=user)
    except Order.DoesNotExist:
        return order
    finally:
        return order

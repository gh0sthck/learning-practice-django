from typing import Optional

from orders.models import Mixin, Order
from users.models import CoffeeUser


def get_order(user: CoffeeUser) -> Optional[Order]:
    order = None
    try:
        order = Order.objects.get(user=user)
    except Order.DoesNotExist:
        return order
    finally:
        return order


def get_mixin(order: Order) -> Optional[Mixin]:
    mixin = None
    try:
        mixin = Mixin.objects.get(order=order)
    except Mixin.DoesNotExist:
        return mixin
    finally:
        return mixin

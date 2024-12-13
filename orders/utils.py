import ast
from typing import Optional
from aogiri.redis_conn import get_redis_connection
from users.models import CoffeeUser


def add_order(user_id: int, order: dict) -> dict[str, dict]:
    """Add dict order to redis database."""
    username = CoffeeUser.objects.get(id=user_id).username
    rc = get_redis_connection()
    rc.set(name=username, value=str(order))
    return {username: order} 
   
    
def get_order(username: Optional[str] = None) -> Optional[dict]:
    """Return dict representation order by username from redis database."""
    if username: 
        rc = get_redis_connection()
        order: Optional[bytes] = rc.get(name=username)
        if order:
            order_decoded = order.decode("utf-8")
            order: dict = ast.literal_eval(order_decoded)
            order["username"] = username
            return order

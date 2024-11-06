import os
from typing import Optional
from dotenv import load_dotenv
import redis

load_dotenv()

redis_host = os.getenv("REDIS_HOST")
redis_port = int(os.getenv("REDIS_PORT"))
redis_password = os.getenv("REDIS_PASSWORD")


def get_redis_connection() -> Optional[redis.Redis]:
    """Return Redis class connection to database."""
    try:
        r = redis.Redis(
            host=redis_host,
            port=redis_port,
        )
    except redis.ConnectionError:
        r = None
    finally:
        return r

import redis
from com.hc_fast.utils.creational.singleton.redis_singleton import REDIS_URL

redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)

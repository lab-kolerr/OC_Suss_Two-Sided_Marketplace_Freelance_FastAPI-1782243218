from redis import Redis
from time import time

class RateLimiter:
    def __init__(self, redis: Redis, max_requests: int, period: int):
        self.redis = redis
        self.max_requests = max_requests
        self.period = period

    async def is_allowed(self, key: str) -> bool:
        now = time()
        bucket_key = f'rate_limit:{key}'
        current = self.redis.get(bucket_key)
        if current is None:
            self.redis.set(bucket_key, 1, ex=self.period)
            return True
        elif int(current) < self.max_requests:
            self.redis.incr(bucket_key)
            return True
        return False
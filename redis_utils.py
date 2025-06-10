
import os
import redis

REDIS_KEY = "sent_gift_ids"

# Подключение к Redis через переменную окружения REDIS_URL
redis_client = redis.Redis.from_url(os.getenv("REDIS_URL"), decode_responses=True)

def is_gift_sent(gift_id: str) -> bool:
    return redis_client.sismember(REDIS_KEY, gift_id)

def mark_gift_as_sent(gift_id: str):
    redis_client.sadd(REDIS_KEY, gift_id)

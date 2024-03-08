#!/usr/bin/env python3
"""redis instance"""
import redis
import uuid
from typing import Union


class Cache:
    """redis cache"""

    def __init__(self):
        """initialize redis instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate random key and store data in redis"""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

#!/usr/bin/env python3
"""redis instance"""
import redis
import uuid
from typing import Union, Callable


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
    
    def get(self, key: str, fn: callable = None):
        """get data from redis and transform it(optional) using fn"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> str:
        """get data from redis and transform it to string"""
        return self.get(key, str)
    
    def get_int(self, key: str) -> int:
        """get data from redis and transform it to int"""
        return self.get(key, int)

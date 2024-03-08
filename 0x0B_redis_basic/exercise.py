#!/usr/bin/env python3
"""redis instance"""
import redis
import uuid
from typing import Union, Callable
import functools


def count_calls(method: Callable) -> Callable:
    """count calls decorator"""

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    
    return wrapper


def call_history(method: Callable) -> Callable:
    """save the call history of different function call"""

    @functools.wraps(method)
    def wrapper(*args):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        args[0]._redis.rpush(input_key, str(args[1:]))
        output = method(*args);
        args[0]._redis.rpush(output_key, output)
    
    return wrapper



class Cache:
    """redis cache"""

    def __init__(self):
        """initialize redis instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate random key and store data in redis"""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    @count_calls
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

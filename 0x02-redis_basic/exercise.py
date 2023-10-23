#!/usr/bin/env python3
"""Exercise """
import redis
import uuid
from typing import Union, Callable
from functools import wraps


class Cache:
    """ Cache class"""

    def __init__(self):
        """Initializes cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def count_calls(fn: Callable) -> Callable:
        """Decorator function"""
        @wraps(fn)
        def wrapper(self, *args, **kwargs):
            key = fn.__qualname__
            self._redis.incr(key)
            return fn(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data in dataset"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """get data from dataset"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            data = fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """get string data from dataset"""
        return self.get(key, fn=lambda x: x.decode())

    def get_int(self, key: str) -> Union[int, None]:
        """get integer data from dataset"""
        return self.get(key, fn=lambda x: int(x))

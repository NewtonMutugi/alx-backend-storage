#!/usr/bin/env python3
"""Writing strings to Redis"""
from typing import Callable, Optional, Union
import redis
import uuid


class Cache:
    """Cache class"""

    def __init__(self) -> None:
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        """Store data in Redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, int, float, bytes]:
        """Get data from Redis"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

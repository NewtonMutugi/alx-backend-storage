#!/usr/bin/env python3
"""Exercise """
import redis
import uuid
from typing import Union


class Cache:
    """ Cache class"""

    def __init__(self):
        """Initializes cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data in dataset"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

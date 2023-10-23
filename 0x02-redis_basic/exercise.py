#!/usr/bin/python3
"""Writing strings to Redis"""
import redis
import uuid


class Cache:
    """Cache class"""

    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """Store data in Redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key):
        """Get data from Redis"""
        data = self._redis.get(key)
        return data.decode("utf-8")

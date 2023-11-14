#!/usr/bin/env python3
"""Redis basics"""

import redis
import uuid
from typing import Union, Callable

class Cache:
    """Redis basics"""
    def __init__(self):
        """Redis basics"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Redis basics"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """Redis basics"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            data = fn(data)
        return data
    
    def get_int(self, key: str):
        """Redis oo"""
        return self.get(key, int)

    def get_str(self, key):
        """All redis"""
        return self.get(key, str)
#!/usr/bin/env python3
"""Redis basics"""

import redis
import uuid
import functools
from typing import Union, Callable

def count_calls(method: Callable) -> Callable:
    """Decorator that counts the number off calls"""
    @functools.wraps(method)
    def wrapped(self, *args, **kwargs):
        """Decorator that counts the number off calls"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapped


def call_history(method: Callable) -> Callable:
    """Call history"""
    @functools.wraps(method)
    def rep(self, *args, **kwargs):
        """All internal"""
        name = method.__qualname__
        self._redit.rpush(f"{name}:inputs", str(args))
        res = method(self, *args)
        self._redit.rpush(f"{name}:outputs", res)
        return res
    return rep

class Cache:
    """Redis basics"""
    def __init__(self):
        """Redis basics"""
        self._redis = redis.Redis()
        self._redis.flushdb()
    @count_calls
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

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


def replay(method: Callable):
    """List the call history of a function"""
    if method is None or not hasattr(method, '__self__'):
        return
    red = getattr(method.__self__, '_redis', None)
    if not isinstance(red, redis.Redis):
        return
    name = method.__qualname__
    # red = Cache()._redis
    # red.flushdb()
    inputs = red.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
    outputs = red.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)
    count = len(inputs)
    print(f"{name} was called {count} times:")
    for i in range(count):
        inp = inputs[i].decode()
        outp = outputs[i].decode()
        print(f"{name}(*{inp}) -> {str(outp)}")


def call_history(method: Callable) -> Callable:
    """Call history"""
    @functools.wraps(method)
    def rep(self, *args, **kwargs):
        """All internal"""
        name = method.__qualname__
        self._redis.rpush(f"{name}:inputs", str(args))
        res = method(self, *args)
        self._redis.rpush(f"{name}:outputs", str(res))
        return res
    return rep


class Cache:
    """Redis basics"""

    def __init__(self):
        """Redis basics"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Redis basics"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        # print(self.get.__qualname__)
        return key

    def get(self,
            key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
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


if __name__ == "__main__":
    cache = Cache()

    # # cache = Cache()
    cache.store("foo")
    cache.store("bar")
    cache.store(42)
    replay(cache.store)

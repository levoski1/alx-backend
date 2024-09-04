#!/usr/bin/env python3
"""Least Recently Used caching module.
"""
from collections import OrderedDict
from basecaching import BaseCaching


class LRUCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LRU
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first = next(iter(self.cache_data))
                print(f"DISCARD: {first}")
                del self.cache_data[first]
            self.cache_data[key] = item
            self.cache_data.move_to_end(key,last=True)

    def get(self, key):
        if not key in self.cache_data or key == None:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value

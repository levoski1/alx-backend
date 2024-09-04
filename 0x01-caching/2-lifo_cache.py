#!/usr/bin/env python3
"""Last In First Out (LIFO) caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LIFO
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache using LIFO.
        """
        if key is None or item is None:
            return  # Do nothing if key or item is None

        # Add or update the item in the cache
        self.cache_data[key] = item

        # If the cache size exceeds the maximum items limit
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the most recently added item (last item)
            last_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is None or key not in self.cache_data:
            return None  # Return None if key is not found

        return self.cache_data[key]

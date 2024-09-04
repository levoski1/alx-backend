#!/usr/bin/env python3
"""
Module: fifo_cache
This module implements a FIFO (First-In-First-Out) cache.
"""

from basecaching import BaseCaching
from typing import Dict, Tuple, List, Any

class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching.
    Implements a FIFO caching mechanism where the oldest item is discarded first.
    """
    
    def __init__(self) -> None:
        """
        Initializes an instance of FIFOCache.
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item) -> None:
        """
        Adds an item to the cache with the specified key.

        If the cache reaches its maximum capacity, the oldest item is discarded.

        Args:
            key (str): The key for the cache item.
            item (any): The item to be cached.

        Returns:
            None
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                first = next(iter(self.cache_data))
                print(f'Discard: {first}')
                del self.cache_data[first]
            
            self.cache_data[key] = item

    def get(self, key) -> Dict[str, Any]:
        """
        Retrieves an item from the cache by its key.

        Args:
            key (str): The key for the cache item to retrieve.

        Returns:
            The cached item, or None if the key is not found.
        """
        return self.cache_data.get(key, None)

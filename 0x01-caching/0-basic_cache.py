#!/usr/bin/env python3
"""
Module: basic_cache
This module provides a BasicCache class for caching data.
"""

from basecaching import BaseCaching
from typing import Dict, Tuple, List

class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching.
    Implements a simple caching mechanism.
    """
    
    def __init__(self) -> Dict[str, str]:
        """
        Initializes an instance of BasicCache.
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item) -> None:
        """
        Adds an item to the cache with the specified key.

        Args:
            key (str): The key for the cache item.
            item (any): The item to be cached.

        Returns:
            None
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key) -> str:
        """
        Retrieves an item from the cache by its key.

        Args:
            key (str): The key for the cache item to retrieve.

        Returns:
            The cached item, or None if the key is not found.
        """
        return self.cache_data.get(key) if key else None

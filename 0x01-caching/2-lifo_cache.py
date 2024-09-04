from basecaching import BaseCaching

class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last = list(self.cache_data)[-1]
                print(f"DISCARD: {last}")
                del self.cache_data[last]
            self.cache_data[key] = item
                
    def get(self, key):
        if key:
            return self.cache_data[key]

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the accessed key to the end (most recent)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Move existing key to end before updating
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        # If we exceeded capacity, pop the first item (least recent)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
            

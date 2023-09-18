# https://leetcode.com/problems/lru-cache/

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        value = self.cache.get(key, -1)
        if value == -1:
            return value
        del self.cache[key]
        self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = value
            return

        length = len(self.cache)
        self.cache[key] = value

        if length < self.capacity:
            return

        del self.cache[next(iter(self.cache))]
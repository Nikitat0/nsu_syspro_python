from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity=16):
        self.dict = OrderedDict()
        self.capacity = capacity

    def put(self, key, value):
        self.dict[key] = value
        self.dict.move_to_end(key)
        if len(self.dict) > self.capacity:
            self.dict.popitem(last=False)

    def get(self, key):
        if key not in self.dict:
            return None
        self.dict.move_to_end(key)
        return self.dict[key]


cache = LRUCache(2)
cache.put(1, "a")
cache.put(2, "b")
cache.get(1)
cache.put(3, "c")
assert cache.get(1) == "a"
assert cache.get(2) == None
assert cache.get(3) == "c"

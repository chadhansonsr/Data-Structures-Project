from collections import OrderedDict


class LRU_Cache(object):

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.our_cache = OrderedDict()

    def get(self, key):
        if key not in self.our_cache:
            return -1
        else:
            self.our_cache.move_to_end(key)
            return self.our_cache[key]

    def set(self, key, value):
        self.our_cache[key] = value
        self.our_cache.move_to_end(key)
        if len(self.our_cache) > self.capacity:
            self.our_cache.popitem(last=False)


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache.our_cache)

our_cache.get(1)  # returns 1
our_cache.get(2)  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache
print(our_cache.our_cache)

our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.get(3))  # returns -1 because 3 was the LRU entry
print(our_cache.our_cache)

# Test Case 1
our_cache.set(7, 7)
print(our_cache.get(7))
print(our_cache.our_cache)
# Test Case 2
our_cache.set(8, "test")
print(our_cache.get(8))
print(our_cache.our_cache)
# Test Case 3
our_cache.set(9, 8675309)
print(our_cache.get(9))
print(our_cache.our_cache)
# Test Case 4
print(our_cache.get(3))
# Test Case 5
print(our_cache.get(5))

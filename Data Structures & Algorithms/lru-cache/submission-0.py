class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key) # moving newly used one at the end of list, think of it as queue where new adds at end, we can do opposite too like moving newlyused to front : self.cache.move_to_end(key,last = False)
        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False) # removing the least used item, which is at front of list, as we have the oldest value at front of queue, we can do reverse too as moving least to last and remove it as: self.cache.move_to_end(last=True)

        

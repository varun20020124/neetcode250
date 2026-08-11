class MyHashMap:

    def __init__(self):
        self.n = 997
        self.hashmap = [None] * self.n

    def put(self, key: int, value: int) -> None:
        index = key % self.n
        self.hashmap[index] = value

    def get(self, key: int) -> int:
        index = key % self.n
        if self.hashmap[index] is not None:
            return self.hashmap[index]
        else:
            return -1

    def remove(self, key: int) -> None:
        index = key % self.n
        if self.hashmap[index] is not None:
            self.hashmap[index] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
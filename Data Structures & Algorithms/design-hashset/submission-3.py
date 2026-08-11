class MyHashSet:

    def __init__(self):
        self.n = 1000
        self.buckets = [[] for _ in range(self.n)]

    def add(self, key: int) -> None:
        index = key % self.n
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = key % self.n
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key%self.n
        if key in self.buckets[index]:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
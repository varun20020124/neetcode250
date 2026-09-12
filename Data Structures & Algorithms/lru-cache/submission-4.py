class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        self.left = ListNode(0,0) # LRU side
        self.right = ListNode(0,0) # MRU side
        self.left.next = self.right
        self.right.prev = self.left

    def add(self, node):
        # insert right before self.right
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def remove(self,node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        
    def get(self, key: int) -> int:
        if key not in self.cache: 
            return -1
        node = self.cache[key]
        # Move to mru position since it is accessed using the get method
        self.remove(node)
        self.add(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = ListNode(key,value)
        self.cache[key] = node
        self.add(node)

        # if capacity is exceeded
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
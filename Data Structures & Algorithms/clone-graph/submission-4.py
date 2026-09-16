"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hashmap = {node : Node(node.val)}
        q = deque()
        q.append(node)
        while q:
            original = q.popleft()
            for adj in original.neighbors:
                if adj not in hashmap:
                    hashmap[adj] = Node(adj.val)
                    q.append(adj)
                copy_original = hashmap[original]
                copy_adj = hashmap[adj]
                copy_original.neighbors.append(copy_adj)
        return hashmap[node]
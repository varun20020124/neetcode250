# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(root):
            if root is None:
                return []
            q = deque([root])
            res = []
            while q:
                node = q.popleft()
                if node:
                    res.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    res.append(None)
            return res
        return bfs(p)==bfs(q)
            
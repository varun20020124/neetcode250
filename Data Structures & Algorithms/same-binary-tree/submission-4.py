# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            for _ in range(len(q1)):
                nodep = q1.popleft()
                nodeq = q2.popleft()
                if nodep is None and nodeq is None:
                    continue
                if nodep is None or nodeq is None or nodep.val!=nodeq.val:
                    return False
                q1.append(nodep.left)
                q2.append(nodeq.left)
                q1.append(nodep.right)
                q2.append(nodeq.right)
        return True
            
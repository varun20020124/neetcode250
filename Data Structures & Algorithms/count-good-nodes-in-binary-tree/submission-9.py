# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:    
        q = deque()
        q.append((root, root.val))
        count = 0
        while q:
            node, largest = q.popleft()
            new_max = max(node.val, largest)
            if node.val>=largest:
                count+=1
            if node.left:
                q.append((node.left,new_max))
            if node.right:
                q.append((node.right,new_max))
        return count
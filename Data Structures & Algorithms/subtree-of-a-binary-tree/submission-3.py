# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p,q):
            d1 = deque([p])
            d2 = deque([q])
            while d1 and d2:
                for _ in range(len(d1)):
                    nodep = d1.popleft()
                    nodeq = d2.popleft()
                    if nodep is None and nodeq is None:
                        continue
                    if nodep is None or nodeq is None or nodep.val!=nodeq.val:
                        return False
                    d1.append(nodep.left)
                    d2.append(nodeq.left)
                    d1.append(nodep.right)
                    d2.append(nodeq.right)
            return True
            
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == subRoot.val:
                if same(node,subRoot):
                    return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
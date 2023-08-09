# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return None

        return self.dfs(root.left, root.right)
    
    def dfs(self, p, q):

        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return self.dfs(p.left, q.right) and self.dfs(p.right, q.left)

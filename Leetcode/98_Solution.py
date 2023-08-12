# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.lst = []
        self.dfs(root)
        
        for i in range(len(self.lst)-1):
            if self.lst[i+1] <= self.lst[i]:
                return False
        return True
        
    
    
    def dfs(self, root):
        if not root:
            return
        
        self.dfs(root.left)
        self.lst.append(root.val)
        self.dfs(root.right)

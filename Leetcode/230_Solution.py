# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []
        self.dfs(root)
        sorted_lst = sorted(self.res)
        return sorted_lst[k - 1]    

    
    def dfs(self, cur):
        if not cur:
            return
        self.dfs(cur.left)
        self.res.append(cur.val)
        self.dfs(cur.right)

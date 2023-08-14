"""
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, sum):
            if not root:
                return False
            sum += root.val
            if not root.left and not root.right and sum == targetSum:
                return True
            else:
                return dfs(root.left, sum) or dfs(root.right, sum)

        return dfs(root, 0)        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root:
            return []

        res = []
        result = []

        def dfs(root, sum=0):

            sum += root.val
            result.append(root.val)

            print(result)

            if not root.left and not root.right and sum == targetSum:
                res.append(result[:])
            if root.left:
                dfs(root.left, sum)
            if root.right:
                dfs(root.right, sum)

            result.pop()
        
        dfs(root)
        return res

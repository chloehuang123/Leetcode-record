# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(root, level):
            if not root:
                return
            if len(res) <= level:
                res.append([])
            res[level].append(root.val)

            if root.left:
                dfs(root.left, level + 1)
            if root.right:
                dfs(root.right, level + 1)
        dfs(root, 0)
        return res[-1][0]

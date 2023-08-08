# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.lst = []
        self.idx = 0 
        self.dfs(root)

    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)
        self.lst.append(root.val)
        self.dfs(root.right)
        


    def next(self) -> int:
        val = self.lst[self.idx]
        self.idx += 1
        return val


    def hasNext(self) -> bool:
        return self.idx < len(self.lst)




# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

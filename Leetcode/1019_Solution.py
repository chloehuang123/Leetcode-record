# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        res = []
        i = 0

        while head:
            while stack and stack[-1][1] < head.val:
                index, value = stack.pop()
                res[index] = head.val
            stack.append((i, head.val))
            res.append(0)
            i += 1
            head = head.next
        
        while stack:
            index, value = stack.pop()
            res[index] = 0

        return res

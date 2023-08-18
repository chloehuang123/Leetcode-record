# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
head -> head.next -> null
curr    temp         pre

pre  <- curr         temp
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre

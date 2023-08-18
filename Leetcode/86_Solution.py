# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()
        right = ListNode()
        lefttail = left
        righttail = right
        curr = head

        while curr:
            if curr.val < x:
                lefttail.next = curr
                lefttail = lefttail.next
            else:
                righttail.next = curr
                righttail = righttail.next
            curr = curr.next

        lefttail.next = right.next
        righttail.next = None

        return left.next

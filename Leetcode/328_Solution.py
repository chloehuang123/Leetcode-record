# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = ListNode()
        left_pointer = left
        right = ListNode()
        right_pointer = right

        i = 0

        while head:
            if i % 2 == 0:
                left_pointer.next = head
                left_pointer = left_pointer.next
            else:
                right_pointer.next = head
                right_pointer = right_pointer.next
            head = head.next
            i += 1
        
        left_pointer.next = right.next
        right_pointer.next = None

        return left.next

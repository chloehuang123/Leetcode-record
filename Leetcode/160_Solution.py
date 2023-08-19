# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeA = headA
        nodeB = headB

        while nodeA != nodeB:
            if nodeA is None:
                nodeA = headB
            else:
                nodeA = nodeA.next
            if nodeB is None:
                nodeB = headA
            else:
                nodeB = nodeB.next
        return nodeB

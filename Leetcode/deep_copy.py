l1 = listNode()
l3 = l1 
l2 = head
while l2:
  l1.next = listNode(l2.val)
  l1 = l1.next
  l2 = l2.next

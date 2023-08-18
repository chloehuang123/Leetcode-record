'''
注意：list1, list2和curr都要持续遍历

'''

var mergeTwoLists = function(l1, l2) {

    var root = new ListNode();
    var temp = root;
    while (l1 && l2) {
        if (l1.val < l2.val) {
            temp.next = l1;
            l1 = l1.next;
        } else {
            temp.next = l2;
            l2 = l2.next;
        }
        temp = temp.next;
    }
    temp.next = l1 || l2;
    return root.next;
    
};

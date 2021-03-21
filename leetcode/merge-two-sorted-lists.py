from node import ListNode

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        newhead = ListNode(-1, None)

        returnhead = newhead
        
        while l1 and l2:
            if l1.val < l2.val:
                newhead.next = l1
                l1 = l1.next
            else:
                newhead.next = l2
                l2 = l2.next
            newhead = newhead.next

        if l1:
            newhead.next = l1

        if l2:
            newhead.next = l2

        return returnhead.next
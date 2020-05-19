from node import ListNode

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newhead = None
        returnhead = None
        if l1 and l2:
            if l1.val < l2.val:
                newhead = l1
                l1 = l1.next
            else:
                newhead = l2
                l2 = l2.next
        elif l1:
            return l1
        elif l2:
            return l2
        else:
            return None

        returnhead = newhead
        
        while True:
            if l1 and l2:
                if l1.val < l2.val:
                    newhead.next = l1
                    l1 = l1.next
                    newhead = newhead.next
                else:
                    newhead.next = l2
                    l2 = l2.next
                    newhead = newhead.next
            else:
                break;

        while l1:
            newhead.next = l1
            l1 = l1.next
            newhead = newhead.next
        while l2:
            newhead.next = l2
            l2 = l2.next
            newhead = newhead.next

        return returnhead
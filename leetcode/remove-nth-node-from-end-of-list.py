from ListNode import ListNode

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head
        
        firstNode = head
        i = 0
        while i < n:
            firstNode = firstNode.next
            i = i + 1
        
        if firstNode is None:
            return head.next

        secondnode = head
        while firstNode.next:
            firstNode = firstNode.next
            secondnode = secondnode.next
        
        secondnode.next = secondnode.next.next
        return temp
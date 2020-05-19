from node import ListNode

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = low = head
        while fast and fast.next:
            fast = fast.next.next
            low = low.next
        
        return low
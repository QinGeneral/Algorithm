# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        prev = head
        h = head.next

        prev.next = h.next
        h.next = prev
        prev.next = self.swapPairs(prev.next)

        return h

        

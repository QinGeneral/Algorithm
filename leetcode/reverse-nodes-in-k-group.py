class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        tail = head
        curK = 0
        while tail:
            curK += 1
            tail = tail.next
            if curK == k:
                break
        if curK < k:
            return head

        newhead = None
        rH = head
        while head:
            temp = head.next
            head.next = newhead
            newhead = head
            head = temp
            if head == tail:
                break
        rH.next = self.reverseKGroup(tail, k)

        return newhead
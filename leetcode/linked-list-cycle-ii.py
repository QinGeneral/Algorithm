class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        seen = set()
        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        return None


# https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode-solution/
class Solution2:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next

        slow = slow.next
        ptr = head
        while slow != ptr:
            ptr = ptr.next
            slow = slow.next

        return ptr
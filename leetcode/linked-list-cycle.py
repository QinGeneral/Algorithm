from ListNode import ListNode


class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True


class Solution3:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True

        return True


def main():
    node7 = ListNode("7", None)
    node6 = ListNode("6", node7)
    # node7.next = node6
    node5 = ListNode("5", node6)
    node4 = ListNode("4", node5)
    node3 = ListNode("3", node4)
    node2 = ListNode("2", node3)
    node1 = ListNode("1", node2)
    node0 = ListNode("0", node1)

    print(hasCycle(node0))


main()

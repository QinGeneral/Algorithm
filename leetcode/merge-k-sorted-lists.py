from ListNode import ListNode


class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        head = None
        for i in lists:
            head = self.mergeTwoLists(head, i)
        return head

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


# 分治法
class Solution2:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists: [ListNode], l, r):
        if l == r:
            return lists[l]
        if l > r:
            return None
        mid = int((l + r) / 2)
        return self.mergeTwoLists(
            self.merge(lists, l, mid), self.merge(lists, mid + 1, r)
        )

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


node1 = ListNode(1)
node1.next = ListNode(4)
node1.next.next = ListNode(5)

node2 = ListNode(1)
node2.next = ListNode(3)
node2.next.next = ListNode(4)

node3 = ListNode(2)
node3.next = ListNode(6)

# node = Solution().mergeKLists([node1, node2, node3])
# node = Solution().mergeKLists([None, None])
node = Solution2().mergeKLists([node1, node2, node3])
while node is not None:
    print(node.val)
    node = node.next
from node import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        newnode = ListNode(0)
        result = newnode
        is_ten = 0
        while l1 or l2:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            sum = l1val + l2val + is_ten
            is_ten = int(sum / 10)
            newnode.next = ListNode(int(sum % 10))
            newnode = newnode.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if is_ten == 1:
            newnode.next = ListNode(1)

        return result.next


# node3 = ListNode(3, None)
# node2 = ListNode(4, node3)
node1 = ListNode(2, None)

nodec = ListNode(4, None)
nodeb = ListNode(6, nodec)
nodea = ListNode(9, nodeb)
solution = Solution()
result = solution.addTwoNumbers(node1, nodea)
while result:
    print(result.val)
    result = result.next

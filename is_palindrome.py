from node import ListNode


# 回文串单链表实现
def is_palindrome_linked_list(head):
    left_head = None
    slow_pointer = head
    fast_pointer = head

    is_odd = True
    while fast_pointer.next is not None:
        if fast_pointer.next.next is not None:
            fast_pointer = fast_pointer.next.next
        else:
            is_odd = False

        old_slow_pointer = slow_pointer
        slow_pointer = slow_pointer.next

        old_slow_pointer.next = left_head
        left_head = old_slow_pointer

        if is_odd == False:
            break

    if is_odd:
        slow_pointer = slow_pointer.next

    while left_head is not None:
        if slow_pointer is None:
            return False

        if left_head.val != slow_pointer.val:
            return False

        left_head = left_head.next
        slow_pointer = slow_pointer.next

    if slow_pointer is not None:
        return False

    return True


def main():
    node7 = ListNode('7', None)
    node6 = ListNode('6', node7)
    node5 = ListNode('5', node6)  # None)
    node4 = ListNode('4', node5)
    node3 = ListNode('3', node4)
    node2 = ListNode('3', node3)
    node1 = ListNode('4', node2)
    node0 = ListNode('5', node1)
    print("is_palindrome", is_palindrome_linked_list(node0))

    # node6 = ListNode('6', None)
    # node5 = ListNode('5', node6)
    # node4 = ListNode('4', node5)  # None)
    # node3 = ListNode('3', node4)
    # node2 = ListNode('2', node3)
    # node1 = ListNode('3', node2)
    # node0 = ListNode('4', node1)
    # print("is_palindrome", is_palindrome_linked_list(node0))


main()

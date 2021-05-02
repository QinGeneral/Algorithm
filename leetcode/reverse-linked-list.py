from ListNode import ListNode


def reverse_single_linked_list(head):

    newhead = None
    while head:
        temp = head.next
        head.next = newhead
        newhead = head
        head = temp

    return newhead


def main():
    node7 = ListNode('7', None)
    node6 = ListNode('6', node7)
    node5 = ListNode('5', node6)
    node4 = ListNode('4', node5)
    node3 = ListNode('3', node4)
    node2 = ListNode('2', node3)
    node1 = ListNode('1', node2)
    node0 = ListNode('0', node1)

    newhead = reverse_single_linked_list(node0)
    while newhead:
        print(newhead.val)
        newhead = newhead.next


main()

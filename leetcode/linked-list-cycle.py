from node import ListNode


def hasCycle(head):

    slowpointer = head
    fastpointer = head

    while slowpointer and fastpointer:
        if fastpointer.next:
            fastpointer = fastpointer.next.next
        else:
            return False

        slowpointer = slowpointer.next

        if slowpointer and fastpointer:
            if slowpointer == fastpointer:
                return True
        else:
            return False

    return False


def main():
    node7 = ListNode('7', None)
    node6 = ListNode('6', node7)
    # node7.next = node6
    node5 = ListNode('5', node6)
    node4 = ListNode('4', node5)
    node3 = ListNode('3', node4)
    node2 = ListNode('2', node3)
    node1 = ListNode('1', node2)
    node0 = ListNode('0', node1)

    print(hasCycle(node0))

main()

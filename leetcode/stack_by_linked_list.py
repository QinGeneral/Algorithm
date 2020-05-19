from node import ListNode


class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, item):
        newnode = ListNode(item)
        if self.head:
            newnode.next = head
            head = newnode
        else:
            self.head = newnode
    
    def pop(self):
        if self.head is None:
            return None
        else:
            result = self.head.val
            self.head = self.head.next
            return result
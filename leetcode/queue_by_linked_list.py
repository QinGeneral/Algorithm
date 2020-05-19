from node import ListNode


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, val):
        newnode = ListNode(val)
        if self.head is None:
            self.tail = self.head = newnode
        else:
            self.tail.next = newnode
            self.tail = self.tail.next
    
    def dequeue(self):
        if self.head:
            result = self.head.val
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return result
        else:
            return None
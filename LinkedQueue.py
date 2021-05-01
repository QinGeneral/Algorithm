from LinkedList import LinkedList


class LinkedQueue:
    head = None
    tail = None

    def enqueue(self, val):
        data = LinkedList(val)
        if self.tail is None:
            self.head = data
            self.tail = data
        else:
            self.tail.next = data
            self.tail = self.tail.next

    def dequeue(self):
        if self.head is None:
            print("queue is empty")
        elif self.head.next is None:
            temp = self.head
            self.head = None
            self.tail = None
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            return temp

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next


queue = LinkedQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.print()
print("--------------")
print(queue.dequeue().val)
print("--------------")
queue.print()
print("--------------")
print(queue.dequeue().val)
print(queue.dequeue().val)
queue.dequeue()

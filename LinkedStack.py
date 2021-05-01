from LinkedList import LinkedList


class LinkedStack:
    head = None
    tail = None

    def push(self, val):
        data = LinkedList(val)
        if self.tail is None:
            self.head = data
            self.tail = self.head
        else:
            self.tail.next = data
            data.prev = self.tail
            self.tail = self.tail.next

    def pop(self):
        if self.tail is None:
            print("stack is empty")
            return None
        elif self.tail.prev is None:
            self.head = None
            temp = self.tail
            self.tail = None
            return temp
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            return temp

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next


stack = LinkedStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print()
print("--------------")
print(stack.pop().val)
print("--------------")
stack.print()
print("--------------")
stack.pop()
stack.print()
print("--------------")
print(stack.pop().val)
print("--------------")
stack.pop()

class MyCircularDeque:
    def __init__(self, k: int):
        self.capacity = k + 1
        self.deque = [0] * self.capacity
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.deque[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        return (self.rear + 1) % self.capacity == self.front


# 有效，但是实际上是 python 数组帮忙做了很多底层工作
# 初始数组长度并不是固定的，而是利用了 python 数组动态添加删除的特性
class MyCircularDeque2:
    def __init__(self, k: int):
        self.deque = []
        self.length = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.insert(0, value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.deque.pop(0)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.deque.pop()
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[-1]

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) == self.length
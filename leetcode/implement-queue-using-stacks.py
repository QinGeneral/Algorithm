class MyQueue:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())

        return self.outStack.pop()

    def peek(self) -> int:
        if self.empty():
            return -1
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())

        return self.outStack[-1]

    def empty(self) -> bool:
        return not self.inStack and not self.outStack
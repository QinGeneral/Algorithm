class CQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def appendTail(self, value: int) -> None:
        self.inStack.append(value)

    def deleteHead(self) -> int:
        if self.empty():
            return -1
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())

        return self.outStack.pop()
    def empty(self) -> bool:
        return not self.inStack and not self.outStack

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
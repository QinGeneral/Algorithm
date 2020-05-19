class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []
        self.min = []

    def push(self, x: int) -> None:
        if len(self.min) == 0 or x <= self.min[len(self.min) - 1]:
            self.min.append(x)
        
        self.array.append(x)

    def pop(self) -> None:
        temp = self.array.pop()
        if temp == self.min[len(self.min) - 1]:
            self.min.pop()

    def top(self) -> int:
        return self.array[len(self.array) - 1]

    def getMin(self) -> int:
        return self.min[len(self.min) - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
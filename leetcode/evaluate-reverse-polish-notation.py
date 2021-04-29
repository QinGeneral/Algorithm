class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        numStack = []
        opts = ["+", "-", "*", "/"]
        for s in tokens:
            if s in opts:
                b = numStack.pop()
                a = numStack.pop()
                numStack.append(self.opt(s, a, b))
            else:
                numStack.append(int(s))
        return numStack[0]

    def opt(self, optS, a, b):
        if optS == "+":
            return a + b
        elif optS == "-":
            return a - b
        elif optS == "*":
            return a * b
        else:
            return int(a / b)


# tokens = ["4","13","5","/","+"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# tokens = ["2", "1", "+", "3", "*"]
print(Solution().evalRPN(tokens))
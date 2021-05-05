class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pushI = 0
        popI = 0
        while pushI < len(pushed) and popI < len(popped):
            if stack and stack[-1] == popped[popI]:
                popI += 1
                stack.pop()
                continue
            if pushed[pushI] != popped[popI]:
                stack.append(pushed[pushI])
                pushI += 1
            else:
                popI += 1
                pushI += 1
        while popI < len(popped):
            if stack and stack[-1] == popped[popI]:
                popI += 1
                stack.pop()
            else:
                return False
        return True


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num)  # num 入栈
            while stack and stack[-1] == popped[i]:  # 循环判断与出栈
                stack.pop()
                i += 1
        return not stack

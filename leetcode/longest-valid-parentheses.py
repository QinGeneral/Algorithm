class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stack = []
        map = {"(": ")", ")": "("}

        cur_length = []
        for ch in s:
            if ch == "(":
                if len(stack) == 0 or stack[-1] == ")":
                    stack.append(ch)
                    cur_length.append(-1)
                else:
                    stack.append(ch)
                    cur_length.append(-1)
            else:
                if len(stack) == 0:
                    cur_length.append(-1)
                elif stack[-1] == "(":
                    cur_length.append(2)
                    if -1 in cur_length:
                        cur_length.reverse()
                        cur_length.remove(-1)
                        cur_length.reverse()
                    stack.pop()
                else:
                    cur_length.append(-1)
        total = 0
        print(cur_length)
        for i in cur_length:
            if i != -1:
                total += i
            else:
                if total > max_length:
                    max_length = total
                total = 0
        if total > max_length:
            max_length = total
        return max_length


print(Solution().longestValidParentheses("())()"))
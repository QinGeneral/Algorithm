class BetterSolution:
    def isValid(self, s: str) -> bool:
        mapping = {"]": "[", "}": "{", ")": "("}
        first = []

        for i in s:
            if i in mapping.keys():
                if len(first) == 0:
                    return False

                if (mapping.get(i) != first.pop()):
                    return False
            else:
                first.append(i)

        if len(first) == 0:
            return True

        return False


class Solution:
    def isValid(self, s: str) -> bool:
        first = []
        for i in s:
            if i == '(':
                first.append(1)
            elif i == ')':
                if len(first) == 0 or first.pop() != 1:
                    return False
            elif i == '{':
                first.append(2)
            elif i == '}':
                if len(first) == 0 or first.pop() != 2:
                    return False
            elif i == '[':
                first.append(3)
            elif i == ']':
                if len(first) == 0 or first.pop() != 3:
                    return False

        if len(first) == 0:
            return True

        return False


Solution = Solution()
print(Solution.isValid("{]}"))

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        self.count = 0
        self.k = k

        num = self.removeOneDigits(num)
        for i in num:
            if len(num) == 1:
                break
            if i == '0':
                num = num[1:]
            else:
                break
        return num

    def removeOneDigits(self, num: str) -> str:
        if self.count == self.k:
            return num
        self.count += 1
        if len(num) == 1:
            return '0'
        elif len(num) == 2:
            if int(num[0]) > int(num[1]):
                return self.removeOneDigits(num[1])
            else:
                return self.removeOneDigits(num[0])
        else:
            orig_length = len(num)
            for j in range(1, len(num)):
                if int(num[j - 1]) > int(num[j]):
                    num = num.replace(num[j - 1], '', 1)
                    break
            if len(num) == orig_length:
                return self.removeOneDigits(num[0: len(num) - 1])
            return self.removeOneDigits(num)


class Solution2:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i in num:
            while k and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)

        if k > 0:
            stack = stack[: -k]

        return ''.join(stack).lstrip('0') or '0'


data = ["1", "1432219", "10200", "10", "1234", "1234"]
ks = [1, 3, 1, 2, 4, 1]
for i in range(len(data)):
    print(Solution2().removeKdigits(data[i], ks[i]))

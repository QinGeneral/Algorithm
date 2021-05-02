INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

# 自动机

class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }
        
    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1

class Solution2:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        isNeg = False
        isBeginNum = False
        newS = ""

        l = 0
        if s[l] == " ":
            for i in range(l, len(s)):
                if s[i] == " ":
                    l += 1
                else:
                    break
        print(s[l:], l, len(s))
        for i in range(l, len(s)):
            ch = s[i]
            print(ch)
            if ch >= "0" and ch <= "9":
                isBeginNum = True
                newS += ch
            elif isBeginNum:
                break
            elif ch == "-":
                isBeginNum = True
                isNeg = True
                l += 1
            elif ch == "+":
                isBeginNum = True
                isNeg = False
                l += 1
            else:
                break
        print(newS)

        if len(newS) == 0:
            return 0
        newL = 0
        if newS[0] == "0":
            for i in range(0, len(newS)):
                if newS[i] == "0":
                    newL += 1
                else:
                    break
                print(newL, newS[i])
        newS = newS[newL:]
        if len(newS) == 0:
            return 0
        print(isNeg, newL, newS)
        min = "2147483648"
        max = "2147483647"
        if isNeg:
            if len(newS) > len(min):
                return -2147483648
            elif len(newS) == len(min):
                for i in range(len(newS)):
                    if newS[i] > min[i]:
                        return -2147483648
                    elif newS[i] == min[i]:
                        continue
                    else:
                        break
                return -int(newS)
            else:
                return -int(newS)
        else:
            if len(newS) > len(max):
                return 2147483647
            elif len(newS) == len(max):
                for i in range(len(newS)):
                    if newS[i] > max[i]:
                        return 2147483647
                    elif newS[i] == max[i]:
                        continue
                    else:
                        break
                return int(newS)
            else:
                return int(newS)


print(Solution().myAtoi(" -42"))
print(Solution().myAtoi("+-42"))
print(Solution().myAtoi("+ 42"))
print(Solution().myAtoi("  0000000000012345678"))
print(Solution().myAtoi("010"))
print(Solution().myAtoi("    -88827   5655  U"))
print('------------------')
print(Solution().myAtoi("1095502006p8"))

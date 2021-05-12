# 递归 + 缓存
class Solution:
    map = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n in self.map:
            return self.map[n]
        else:
            value = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.map[n] = value
            return value


# 递推
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        stair = [0] * (n + 1)
        stair[1] = 1
        stair[2] = 2
        for i in range(3, n + 1):
            stair[i] = stair[i - 1] + stair[i - 2]

        return stair[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        stair1 = 1
        stair2 = 2
        finalCount = 0
        for i in range(3, n + 1):
            finalCount = stair1 + stair2
            stair1 = stair2
            stair2 = finalCount

        return finalCount
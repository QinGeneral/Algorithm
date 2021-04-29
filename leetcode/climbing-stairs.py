class Solution:
    map = {1: 1, 2: 2}
    def climbStairs(self, n: int) -> int:
        if n in self.map:
            return self.map[n]
        else:
            value = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.map[n] = value
            return value
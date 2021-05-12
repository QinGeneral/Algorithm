# 动态规划
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], dp[j] * dp[i - j])

        print(dp)
        return dp[n]


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [0] * (n + 1)
        dp[1] = 0
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], max(j * dp[i - j], j * (i - j)))

        print(dp)
        return dp[n]


# 贪心
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        threeCount = n // 3
        left = n % 3
        twoCount = 0
        if left == 0:
            pass
        elif left == 1:
            threeCount -= 1
            twoCount = 2
        else:
            twoCount = 1

        max = pow(3, threeCount)
        max = max << twoCount
        return max


print(Solution().cuttingRope(2))
print(Solution().cuttingRope(8))
print(Solution().cuttingRope(10))
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        max = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i] and prices[j] - prices[i] > max:
                    max = prices[j] - prices[i]

        return max


class Solution:
    def maxProfit(self, prices: [int]) -> int:
        dp = [[0, float("-inf")] for _ in range(len(prices))]
        dp[0][1] = prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], prices[i] - dp[i - 1][1])
            dp[i][1] = min(dp[i - 1][1], prices[i])

        return dp[len(prices) - 1][0]


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))

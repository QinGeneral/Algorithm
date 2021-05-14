class Solution:
    def maxProfit(self, prices: [int]) -> int:
        dp = [[[0] * 2 for _ in range(2)] for _ in range(len(prices))]
        for i in range(2):
            dp[0][i][0] = 0
            dp[0][i][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][0][0])
            dp[i][1][1] = max(dp[i - 1][1][0] - prices[i], dp[i - 1][1][1])
            dp[i][0][0] = dp[i - 1][1][1] + prices[i]
        maxProfit = 0
        for i in range(2):
            maxProfit = max(maxProfit, dp[len(prices) - 1][i][0])
        return maxProfit


print(Solution().maxProfit([1, 2, 3, 0, 2]))
print(Solution().maxProfit([1, 2, 3, 4, 5]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))

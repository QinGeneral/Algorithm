class Solution:
    def maxProfit(self, prices: [int]) -> int:
        maxTradeCount = 2
        dp = [[[0] * 2 for _ in range(maxTradeCount + 1)] for _ in range(len(prices))]
        for i in range(maxTradeCount + 1):
            dp[0][i][0] = 0
            dp[0][i][1] = -prices[0]
        print(dp)
        for i in range(1, len(prices)):
            for j in range(0, maxTradeCount + 1):
                print(i, j)
                dp[i][j][0] = max(
                    dp[i - 1][j][0], (dp[i - 1][j - 1][1] + prices[i]) if j > 0 else 0
                )
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] - prices[i])
        print(dp)
        maxProfit = 0
        for i in range(maxTradeCount + 1):
            maxProfit = max(maxProfit, dp[len(prices) - 1][i][0])
        return maxProfit


print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
print(Solution().maxProfit([1, 2, 3, 4, 5]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))

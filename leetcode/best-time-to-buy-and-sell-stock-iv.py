class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        maxTradeCount = k
        dp = [[[0] * 2 for _ in range(maxTradeCount + 1)] for _ in range(len(prices))]
        for i in range(maxTradeCount + 1):
            dp[0][i][0] = 0
            dp[0][i][1] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(0, maxTradeCount + 1):
                dp[i][j][0] = max(
                    dp[i - 1][j][0], (dp[i - 1][j - 1][1] + prices[i]) if j > 0 else 0
                )
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] - prices[i])
        maxProfit = 0
        for i in range(maxTradeCount + 1):
            maxProfit = max(maxProfit, dp[len(prices) - 1][i][0])
        return maxProfit
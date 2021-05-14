class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if not prices:
            return 0
        dp = [[0, float("-inf")] for _ in range(len(prices))]
        dp[0][1] = prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], prices[i] - dp[i - 1][1])
            dp[i][1] = min(dp[i - 1][1], prices[i])

        return dp[len(prices) - 1][0]
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        money = 0
        curM = -1
        for i in range(0, len(prices) - 1):
            if prices[i] > prices[i + 1]:
                if curM > -1:
                    money += prices[i] - curM
                    curM = -1
            else:
                if curM == -1:
                    curM = prices[i]
        if curM > -1 and prices[-1] > curM:
            money += prices[-1] - curM
            curM = -1
        return money


# 贪心算法
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        money = 0
        for i in range(0, len(prices) - 1):
            if prices[i] < prices[i + 1]:
                money += prices[i + 1] - prices[i]
        return money


# 动态规划
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        dp = [0] * len(prices)
        dp[0] = 0
        for i in range(1, len(prices)):
            todayProfit = prices[i] - prices[i - 1]
            dp[i] = dp[i - 1] + (todayProfit if todayProfit > 0 else 0)
        return dp[len(prices) - 1]


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
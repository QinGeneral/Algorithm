class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        money = 0
        for i in range(0, len(prices) - 1):
            if prices[i] < prices[i + 1]:
                money += prices[i + 1] - prices[i]
        return money
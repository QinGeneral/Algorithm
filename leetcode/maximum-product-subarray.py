# 暴力递归
class Solution:
    def maxProduct(self, nums: [int]) -> int:
        finalMaxV = nums[0]
        for i in range(len(nums)):
            maxV = nums[i]
            curValue = nums[i]
            for j in range(i + 1, len(nums)):
                curValue = curValue * nums[j]
                maxV = max(maxV, curValue)
            print(i, maxV)
            finalMaxV = max(finalMaxV, maxV)
        return finalMaxV


class Solution:
    def maxProduct(self, nums: [int]) -> int:
        dp = [[float("inf"), float("-inf")] for _ in range(len(nums))]
        # 0 存储 min，1 存储 max
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        maxValue = nums[0]
        for i in range(1, len(nums)):
            # if nums[i] > 0:
            #     dp[i][0] = min(dp[i][0], dp[i - 1][0] * nums[i], nums[i])
            #     dp[i][1] = max(dp[i][1], dp[i - 1][1] * nums[i], nums[i])
            # else:
            #     dp[i][0] = min(dp[i][0], dp[i - 1][1] * nums[i], nums[i])
            #     dp[i][1] = max(dp[i][1], dp[i - 1][0] * nums[i], nums[i])
            temp1 = dp[i - 1][0] * nums[i]
            temp2 = dp[i - 1][1] * nums[i]
            dp[i][0] = min(temp1, temp2, nums[i])
            dp[i][1] = max(temp1, temp2, nums[i])
            maxValue = max(maxValue, dp[i][1])
        return maxValue


# 扩展性不如上一个强，只局限于这个维度的问题
class Solution:
    def maxProduct(self, nums: [int]) -> int:
        curMax = curMin = maxValue = nums[0]
        for i in range(1, len(nums)):
            curMax = curMax * nums[i]
            curMin = curMin * nums[i]
            curMin, curMax = min(curMax, curMin, nums[i]), max(curMax, curMin, nums[i])
            maxValue = max(maxValue, curMax)
        return maxValue


print(Solution().maxProduct([2, 3, -2, 4]))
print(Solution().maxProduct([-2, 0, -1]))
print(Solution().maxProduct([0, 2]))
print(Solution().maxProduct([-2, 3, -4]))
print(Solution().maxProduct([2, -5, -2, -4, 3]))

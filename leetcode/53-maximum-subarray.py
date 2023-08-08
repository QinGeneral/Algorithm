# 动态规划
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        maxN = dp[0]

        print(nums)
        print(dp)
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            maxN = max(maxN, dp[i])
            print(dp, maxN)

        return maxN


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

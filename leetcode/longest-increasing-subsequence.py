class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
print(Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))


class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        lis = []
        for i in range(0, len(nums)):
            if (not lis) or nums[i] > lis[-1]:
                lis.append(nums[i])
                continue
            if lis[0] > nums[i]:
                lis[0] = nums[i]
                continue
            index = self.findFirstBig(lis, nums[i])
            print(index, lis)
            if index == 0 or lis[index - 1] < nums[i]:
                lis[index] = nums[i]

        print(lis)
        return len(lis)

    def findFirstBig(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start < end - 1:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid
            else:
                end = mid
        return end


print(Solution().lengthOfLIS([4, 10, 4, 3, 8, 9]))
print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
print(Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
print(Solution().lengthOfLIS([1, 2, -10, -8, -7]))

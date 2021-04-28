class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        n = len(nums)
        if n < 3:
            return []
        result = []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            kIndex = n - 1
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                while j < kIndex and nums[i] + nums[j] + nums[kIndex] > 0:
                    kIndex = kIndex - 1;
                if j == kIndex:
                    break
                if nums[i] + nums[j] + nums[kIndex] == 0:
                    temp = [nums[i], nums[j], nums[kIndex]]
                    if temp not in result:
                        result.append(temp)
        return result


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
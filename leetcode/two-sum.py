class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

class Solution2:
    def twoSum(self, nums: [int], target: int) -> [int]:
        s = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in s and i != s[t]:
                return [i, s[t]]
            s[nums[i]] = i
        return []

print(Solution2().twoSum([2, 5, 5, 11], 10))
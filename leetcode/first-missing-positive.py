class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        nums.sort()
        if nums[0] > 1:
            return 1
        for i in range(0, len(nums)):
            if i > 0 and nums[i - 1] <= 0 and nums[i] > 1:
                return 1

            if i > 0 and nums[i - 1] >= 0 and nums[i] - nums[i - 1] > 1:
                return nums[i - 1] + 1

        if nums[-1] < 1:
            return 1
        return nums[-1] + 1


class Solution2:
    def firstMissingPositive(self, nums: [int]) -> int:
        map = {}
        for i in nums:
            map[i] = 1
        k = 1
        while True:
            if k not in map:
                return k
            k += 1


class Solution3:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 1

        for i in range(len(nums)):
            num = abs(nums[i])
            if num <= len(nums):
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        return len(nums) + 1


print(Solution().firstMissingPositive([7, 8, 9, 11, 12]))

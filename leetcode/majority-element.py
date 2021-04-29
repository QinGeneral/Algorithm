# 时间复杂度 O(n)
# 空间复杂度 O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        pivot = len(nums) / 2
        for i in map:
            if map[i] > pivot:
                return i


# 时间复杂度 O(nlogn)
# 空间复杂度 O(1)
# 时间换空间
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums) / 2)]

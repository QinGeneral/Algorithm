class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return l


print(Solution().searchInsert([1, 3, 5, 7], 1))
print(Solution().searchInsert([1, 3, 5, 7], 5))
print(Solution().searchInsert([1, 3, 5, 7], 7))
print(Solution().searchInsert([1, 3, 5, 7], 2))
print(Solution().searchInsert([1, 3, 5, 7], 0))
print(Solution().searchInsert([1, 3, 5, 7], 9))

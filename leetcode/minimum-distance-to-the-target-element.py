class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min = len(nums)
        for i in range(start, len(nums)):
            if nums[i] == target:
                m = abs(i - start)
                if m < min:
                    min = m
                break
        if min == 0:
            return min
        for i in range(start - 1, -1, -1):
            if nums[i] == target:
                m = abs(i - start)
                if m < min:
                    min = m
                break

        return min


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = len(nums)
        for i, num in enumerate(nums):
            if num == target:
                res = min(res, abs(i - start))
        return res

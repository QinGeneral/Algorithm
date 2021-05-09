# 时间复杂度 O(n)
# 空间复杂度 O(n)
class Solution:
    def majorityElement(self, nums: [int]) -> int:
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
    def majorityElement(self, nums: [int]) -> int:
        nums.sort()
        return nums[int(len(nums) / 2)]


class Solution3:
    def majorityElement(self, nums: [int]) -> int:
        def dc(l, r):
            if l >= r:
                return (nums[l], 1)
            mid = (l + r) // 2
            (lMax, lCount) = dc(l, mid)
            (rMax, rCount) = dc(mid + 1, r)
            if lMax == rMax:
                return (lMax, lCount + rCount)

            lc = 0
            rc = 0
            for i in range(l, r + 1):
                if nums[i] == lMax:
                    lc += 1
                elif nums[i] == rMax:
                    rc += 1
            return (lMax, lc) if lc > rc else (rMax, rc)

        (max, count) = dc(0, len(nums) - 1)
        print(max, count)
        return max


Solution3().majorityElement([6, 5, 5])

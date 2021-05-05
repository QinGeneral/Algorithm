# 时间复杂度 O(n^2)
# 空间复杂度 O(1)
class Solution:
    def threeSum(self, nums: [int], target) -> [[int]]:
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
                while j < kIndex and nums[i] + nums[j] + nums[kIndex] > target:
                    kIndex = kIndex - 1
                if j == kIndex:
                    break
                if nums[i] + nums[j] + nums[kIndex] == target:
                    temp = [nums[i], nums[j], nums[kIndex]]
                    if temp not in result:
                        result.append(temp)
        return result


# 时间复杂度 O(n^2)
# 空间复杂度 O(n)
class Solution2:
    def threeSum(self, nums: [int], target) -> [[int]]:
        n = len(nums)
        if n < 3:
            return []
        result = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            map = {}
            for j in range(i + 1, n):
                t = target - nums[i] - nums[j]
                if t in map and map[t] != j:
                    temp = [nums[i], nums[j], t]
                    temp.sort()
                    if temp not in result:
                        result.append(temp)
                else:
                    map[nums[j]] = j
        return result


print(Solution2().threeSum([-1, 0, 1, 2, -1, -4], 2))
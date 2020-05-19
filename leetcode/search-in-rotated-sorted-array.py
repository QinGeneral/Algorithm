# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/sou-suo-xuan-zhuan-pai-xu-shu-zu-by-leetcode-solut/

class Solution:
    def handle_array(self, nums, target, low, high):
        if (low > high):
            return -1

        mid = int((low + high) / 2)
        if nums[mid] == target:
            return mid
        
        if nums[low] <= nums[mid]:
            if target >= nums[low] and target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if target > nums[mid] and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        return self.handle_array(nums, target, low, high)

    def search(self, nums, target):
            return self.handle_array(nums, target, 0, len(nums) - 1)


class LoopSolution:
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while(low <= high):
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

Solution = Solution()
# print(Solution.search([4,5,6,7,0,1,2], 3))
# print(Solution.search([1, 3], 3))
print(Solution.search([3, 1], 1))
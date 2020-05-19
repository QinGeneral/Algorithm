class BetterSolution:
    def removeElement(self, nums, val: int) -> int:
        length_range = range(len(nums))
        length = 0

        for i in length_range:
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1

        return length


class Solution:
    def removeElement(self, nums, val: int) -> int:
        length_range = range(len(nums))
        not_val_num = 0

        for i in length_range:
            if nums[i] != val:
                not_val_num += 1
                for j in range(0, i):
                    if nums[j] == val:
                        nums[j] = nums[i]
                        nums[i] = val
                        break
        return not_val_num


Solution = Solution()
print(Solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))

BetterSolution = BetterSolution()
print(BetterSolution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))

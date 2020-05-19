class BetterSolution:
    def removeDuplicates(self, nums):

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            
        return i + 1

class Solution:
    def removeDuplicates(self, nums):

        i = len(nums) - 1
        length = len(nums)
        while(i > 0):

            j = i - 1
            while j >= 0:
                if nums[i] == nums[j]:
                    j -= 1
                else:
                    break
            
            newlength = length - (i - 1 - j)
            temp = j
            for k in range(i, length):
                nums[j + 1] = nums[k]
                j += 1
            i = temp
            length = newlength
            
        return length
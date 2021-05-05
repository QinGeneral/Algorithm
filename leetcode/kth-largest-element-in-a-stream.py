import heapq


class KthLargest:
    def __init__(self, k: int, nums: [int]):
        self.k = k + 1
        self.nums = nums
        self.array = [0]
        for i in nums:
            self.insert(self.array, i)
        while len(self.array) > self.k:
            self.pop(self.array)

    def add(self, val: int) -> int:
        self.insert(self.array, val)
        while len(self.array) > self.k:
            self.pop(self.array)
        return self.array[1]

    def insert(self, nums, val):
        nums.append(val)
        self.moveUp(nums, len(nums) - 1)

    def pop(self, nums):
        nums[1] = nums[-1]
        nums.pop()
        self.moveDown(nums, 1)

    def moveDown(self, nums, i):
        while True:
            targetI = i
            if i * 2 < len(nums) and nums[targetI] > nums[i * 2]:
                targetI = i * 2
            if i * 2 + 1 < len(nums) and nums[targetI] > nums[i * 2 + 1]:
                targetI = i * 2 + 1
            if i == targetI:
                break
            self.swap(nums, i, targetI)
            i = targetI

    def moveUp(self, nums, i):
        while i // 2 >= 1:
            if nums[i] < nums[i // 2]:
                self.swap(nums, i, i // 2)
                i = i // 2
            else:
                break

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp


class KthLargest2:
    def __init__(self, k: int, nums: [int]):
        self.k = k
        self.hq = []
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        ######## 可加可不加
        if len(self.hq) == self.k and val < self.hq[0]:
            return self.hq[0]
        ########
        heapq.heappush(self.hq, val)
        if len(self.hq) > self.k:
            heapq.heappop(self.hq)
        return self.hq[0]


kthLargest = KthLargest2(3, [4, 5, 8, 2])
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))

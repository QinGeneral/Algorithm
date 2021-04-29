import heapq


class Solution:
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        result = []
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        result.append(-q[0][0])
        for i in range(k, len(nums)):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            result.append(-q[0][0])
        return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
# print(Solution().maxSlidingWindow(nums, k))
# print(Solution().maxSlidingWindow([1], 1))
print(Solution().maxSlidingWindow([1, -1], 1))
# print(Solution().maxSlidingWindow([1, -1], 2))

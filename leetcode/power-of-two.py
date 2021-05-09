class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        if n < 0:
            return False
        while n != 0:
            count += 1
            n = n & (n - 1)
        return count == 1


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (n - 1) == 0

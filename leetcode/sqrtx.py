class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        start = 1
        end = x
        while start < end - 1:
            mid = int((end - start) / 2) + start
            sq = mid * mid
            if sq == x:
                return mid
            elif sq > x:
                end = mid
            else:
                start = mid

        return start

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


class Solution2:
    def mySqrt(self, x: int, n) -> int:
        if x == 0:
            return 0
        start = 1
        end = x
        while start < end:
            mid = (end - start) / 2 + start
            sq = mid * mid
            print(start, end, mid, sq)
            if len(str(mid).split(".")[1]) >= n:
                return mid
            if sq == x:
                return mid
            elif sq > x:
                end = mid
            else:
                start = mid

        return start


class Solution3:
    def mySqrt(self, x: int, n) -> int:
        if x == 0:
            return 0
        start = 1
        end = x
        while (end - start) > pow(10, -n):
            mid = (end - start) / 2 + start
            sq = mid * mid
            if sq == x:
                return mid
            elif sq > x:
                end = mid
            else:
                start = mid
            print(end - start, start, end, mid, sq)

        return start


# 牛顿迭代法
class Solution4:
    def mySqrt(self, x):
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return r


print(Solution3().mySqrt(2, 3))
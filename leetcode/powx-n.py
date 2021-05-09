class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        elif n == -1:
            return 1 / x
        elif n == 1:
            return x

        real_n = n
        if n < 0:
            real_n = -n

        half = int(real_n / 2)
        half_sum = self.myPow(x, half)
        sum = half_sum * half_sum
        if int(n % 2) == 1:
            sum = x * sum

        if n < 0:
            sum = 1 / sum

        return sum


class AnotherSolution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        elif n == -1:
            return 1 / x
        elif n == 1:
            return x

        half = int(n / 2)
        half_sum = self.myPow(x, half)
        sum = half_sum * half_sum
        if int(n % 2) == 1:
            if n > 0:
                sum = x * sum
            else:
                sum = 1 / x * sum

        return sum


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        isPositive = n > 0
        if not isPositive:
            n = -n
        if n == 1:
            return x if isPositive else 1 / x
        if n % 2 == 0:
            r = self.myPow(x, n // 2)
            return r * r if isPositive else 1 / (r * r)
        else:
            r = self.myPow(x, n // 2)
            return r * r * x if isPositive else 1 / (r * r * x)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow
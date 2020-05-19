class BetterSolution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        if x < 10:
            return True

        revert = 0
        while(x > revert):
            revert = int(revert * 10) + int(x % 10)
            x = int(x / 10)
        
        return x == revert or x == int(revert / 10)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x < 10:
            return True

        temp = 10
        while True:
            num = int(x / temp)
            if num == 0:
                break

            temp *= 10
        
        temp = int(temp / 10)
        start = 10
        while temp >= start:
            if int(x % start) != int(x / temp):
                return False

            x = int(x % temp)
            x = int(x / start)
            temp = int(temp / 100)
        
        return True


Solution = Solution()
print(Solution.isPalindrome(1234567654321))

BetterSolution = BetterSolution()
print(BetterSolution.isPalindrome(1234567654321))
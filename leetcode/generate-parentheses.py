class Solution:
    def generateParenthesis(self, n: int) -> [str]:

        result = []

        leftCount = n
        rightCount = n

        def recursion(curStr, leftCount, rightCount):
            if leftCount == 0 and rightCount == 0:
                result.append(curStr)
                return
            if leftCount > 0:
                recursion(curStr + "(", leftCount - 1, rightCount)
            # rightCount > 0 可以被优化，直接去掉即可，因为 leftcount 肯定 >= 0
            if leftCount < rightCount and rightCount > 0: 
                recursion(curStr + ")", leftCount, rightCount - 1)

        recursion("", leftCount, rightCount)
        return result


class Solution:
    def generateParenthesis(self, n: int) -> [str]:

        result = []

        leftCount = n
        rightCount = n

        def recursion(curStr, leftCount, rightCount):
            if not self.isValid(curStr):
                return
            print(curStr, leftCount, rightCount)
            if leftCount == 0 and rightCount == 0:
                result.append(curStr)
                return
            if leftCount > 0:
                recursion(curStr + "(", leftCount - 1, rightCount)
            if rightCount > 0:
                recursion(curStr + ")", leftCount, rightCount - 1)

        recursion("", leftCount, rightCount)
        return result

    def isValid(self, s: str):
        while "()" in s:
            s = s.replace("()", "")
        if ")" in s:
            return False
        return True


result = Solution().generateParenthesis(4)
print(len(result), result)

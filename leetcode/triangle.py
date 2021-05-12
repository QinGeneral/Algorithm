# 递归 + memo
class Solution:
    def minimumTotal(self, triangle: [[int]]) -> int:
        memo = []
        for i in range(len(triangle)):
            memo.append([None] * len(triangle[i]))

        def dfs(row, column):
            if row < 0:
                return 0
            if row == 0:
                return triangle[0][0]
            if memo[row][column]:
                return memo[row][column]
            count = []
            curValue = triangle[row][column]
            if column != len(triangle[row]) - 1:
                count.append(dfs(row - 1, column) + curValue)
            if column != 0:
                count.append(dfs(row - 1, column - 1) + curValue)
            print(row, count, min(count))
            memo[row][column] = min(count)
            return memo[row][column]

        array = []
        for i in range(len(triangle[-1])):
            array.append(dfs(len(triangle) - 1, i))
        print(array)
        return min(array)


# 动态规划
class Solution:
    def minimumTotal(self, triangle: [[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        memo = []
        for i in range(len(triangle)):
            memo.append([float("inf")] * len(triangle[i]))
        memo[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                curValue = triangle[i][j]
                topValue = float("inf")
                topLeftValue = float("inf")
                if j != 0:
                    topLeftValue = memo[i - 1][j - 1]
                if j != len(triangle[i]) - 1:
                    topValue = memo[i - 1][j]
                memo[i][j] = min(topValue, topLeftValue) + curValue
        print(memo)
        return min(memo[-1])


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(Solution().minimumTotal(triangle))
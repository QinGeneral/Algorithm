class Solution:
    def totalNQueens(self, n: int) -> int:
        chess = [-1] * n
        r = []

        def dfs(chess, row):
            if row == n:
                r.append(chess)
                return
            for column in range(n):
                if isOk(chess, row, column):
                    chess[row] = column
                    dfs(chess, row + 1)

        def isOk(chess, row, column):
            leftUp = column - 1
            rightUp = column + 1
            for i in range(row - 1, -1, -1):
                if chess[i] == column:
                    return False
                if leftUp >= 0:
                    if chess[i] == leftUp:
                        return False
                if rightUp < n and chess[i] == rightUp:
                    return False
                leftUp -= 1
                rightUp += 1
            return True
        dfs(chess, 0)
        return len(r)
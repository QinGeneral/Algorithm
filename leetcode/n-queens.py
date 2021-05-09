class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        chess = [-1] * n
        r = []

        def dfs(chess, row):
            if row == n:
                r.append(getStr(chess))
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
                if leftUp >= 0 and chess[i] == leftUp:
                    return False
                if rightUp < n and chess[i] == rightUp:
                    return False
                leftUp -= 1
                rightUp += 1
            return True

        def getStr(array):
            result = []
            for i in array:
                s = ""
                for j in range(0, i):
                    s += "."
                s += "Q"
                for j in range(i + 1, len(array)):
                    s += "."
                result.append(s)
            return result

        dfs(chess, 0)
        return r


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        chess = [-1] * n
        r = []

        columnSet = set()
        pieSet = set()
        naSet = set()

        def dfs(chess, row):
            if row == n:
                r.append(getStr(chess))
                return
            for column in range(n):
                if (
                    column not in columnSet
                    and row + column not in pieSet
                    and row - column not in naSet
                ):
                    chess[row] = column
                    columnSet.add(column)
                    pieSet.add(row + column)
                    naSet.add(row - column)
                    dfs(chess, row + 1)
                    columnSet.remove(column)
                    pieSet.remove(row + column)
                    naSet.remove(row - column)

        def getStr(array):
            result = []
            for i in array:
                s = ""
                for j in range(0, i):
                    s += "."
                s += "Q"
                for j in range(i + 1, len(array)):
                    s += "."
                result.append(s)
            return result

        dfs(chess, 0)
        return r

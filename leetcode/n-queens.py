class Solution:
    def solveNQueens(self, n: int) -> [[str]]:

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
    def solveNQueens(self, n: int) -> [[str]]:

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

# 位运算版本，输出还没有搞定 todo
class Solution:
    def solveNQueens(self, n: int) -> [[str]]:

        r = []

        self.rowStr = []
        def dfs(row, col, pie, na):
            if row == n:
                r.append(self.rowStr)
                print(self.rowStr)
                self.rowStr = []
                return
            # 得到空位
            bits = (~(col | pie| na)) & ((1 << n) - 1)
            while bits:
                # 得到最后一个 1
                p = bits & -bits
                if row == 0:
                    self.rowStr = []
                self.rowStr.append(bin(p)[2:].zfill(n).replace('1', 'Q').replace('0', '.'))
                print(row, self.rowStr)
                dfs(row + 1, col | p, (pie | p) << 1, (na | p) >> 1)
                # 去掉最后一位 1
                bits &= bits - 1
            if row == 0:
                self.rowStr = []
        dfs(0, 0, 0, 0)
        return r


print(Solution().solveNQueens(5))
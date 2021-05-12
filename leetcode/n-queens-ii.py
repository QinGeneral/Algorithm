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


class Solution:
    def totalNQueens(self, n: int) -> int:

        self.count = 0
        def dfs(row, col, pie, na):
            if row == n:
                self.count += 1
                return
            # 得到空位
            bits = (~(col | pie | na)) & ((1 << n) - 1)
            while bits:
                # 得到最后一个 1
                p = bits & -bits
                dfs(row + 1, col | p, (pie | p) << 1, (na | p) >> 1)
                # 去掉最后一位 1
                bits &= bits - 1

        dfs(0, 0, 0, 0)
        return self.count
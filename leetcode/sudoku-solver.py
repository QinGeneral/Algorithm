class Solution:
    def solveSudoku(self, board: [[str]]) -> None:
        def solve(board):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == ".":
                        for k in range(0, 9):
                            kChar = str(int("1") + k)
                            if isValid(board, i, j, kChar):
                                board[i][j] = kChar
                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
            return True

        def isValid(board, i, j, ch):
            for index, value in enumerate(board[i]):
                if index == j:
                    continue
                if value == ch:
                    return False
            for index, value in enumerate(board):
                if index == i:
                    continue
                if value[j] == ch:
                    return False
            row = i // 3 * 3
            column = j // 3 * 3
            for rowI in range(row, row + 3):
                for columnJ in range(column, column + 3):
                    if rowI == i and columnJ == j:
                        continue
                    if board[rowI][columnJ] == ch:
                        return False
            return True

        solve(board)


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
Solution().solveSudoku(board)
print(board)
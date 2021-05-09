class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for i in range(m)]
        result = []
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def findS(word, index, i, j, visited):
            print(word, word[index] if index < len(word) else None, i, j)
            if board[i][j] != word[index]:
                return False
            if index == len(word) - 1:
                if word not in result:
                    result.append(word)
                return True
            visited[i][j] = True
            isSuccess = False

            for di, dj in direction:
                newI = i + di
                newJ = j + dj
                if newI < 0 or newI >= m or newJ < 0 or newJ >= n:
                    continue
                if visited[newI][newJ]:
                    continue
                isSuccess = findS(word, index + 1, newI, newJ, visited)
                if isSuccess:
                    break
            visited[i][j] = False
            return isSuccess

        def findWord(word, i, visited):
            for i in range(m):
                for j in range(n):
                    if findS(word, 0, i, j, visited):
                        return True
            return False

        return findWord(word, 0, visited)


class Solution2:
    def exist(self, board: [[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for i in range(m)]
        result = []

        def findS(word, index, i, j, visited):
            # print(word, word[index] if index < len(word) else None, i, j)
            if index == len(word):
                if word not in result:
                    result.append(word)
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            isSuccess = False
            if i - 1 >= 0 and not visited[i - 1][j] and board[i - 1][j] == word[index]:
                visited[i - 1][j] = True
                isSuccess = findS(word, index + 1, i - 1, j, visited)
                visited[i - 1][j] = False
                if isSuccess:
                    return True
            if j - 1 >= 0 and not visited[i][j - 1] and board[i][j - 1] == word[index]:
                visited[i][j - 1] = True
                isSuccess = findS(word, index + 1, i, j - 1, visited)
                visited[i][j - 1] = False
                if isSuccess:
                    return True
            if i + 1 < m and not visited[i + 1][j] and board[i + 1][j] == word[index]:
                visited[i + 1][j] = True
                isSuccess = findS(word, index + 1, i + 1, j, visited)
                visited[i + 1][j] = False
                if isSuccess:
                    return True
            if j + 1 < n and not visited[i][j + 1] and board[i][j + 1] == word[index]:
                visited[i][j + 1] = True
                isSuccess = findS(word, index + 1, i, j + 1, visited)
                visited[i][j + 1] = False
                if isSuccess:
                    return True
            return False

        def findWord(word, i, visited):
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        # print(word, i, j)
                        visited[i][j] = True
                        isSuccess = findS(word, 1, i, j, visited)
                        visited[i][j] = False
                        if isSuccess:
                            return True
            return False

        return findWord(word, 0, visited)


print(Solution().exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"))
print(Solution().exist([["a"]], "a"))

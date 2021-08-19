class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1 = len(word1) + 1
        length2 = len(word2) + 1
        maxCount = length1 if length1 > length2 else length2
        dp = [[0] * length2 for _ in range(length1)]
        for i in range(length1):
            dp[i][0] = i
        for i in range(length2):
            dp[0][i] = i
        dp[0][0] = 0
        word1 = "0" + word1
        word2 = "0" + word2
        for i in range(1, length1):
            for j in range(1, length2):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1, dp[i - 1][j] + 1
                    )
        print(dp)
        return dp[length1 - 1][length2 - 1]


print(Solution().minDistance("horse", "ros"))
print(Solution().minDistance("", "a"))
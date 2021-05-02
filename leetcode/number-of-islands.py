class Solution:
    def numIslands(self, grid: [[str]]) -> int:

        self.island = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    self.island += 1
                    self.erase(i, j, grid)
        return self.island

    def erase(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
            return
        if grid[i][j] == "1":
            grid[i][j] = 0
            self.erase(i - 1, j, grid)
            self.erase(i + 1, j, grid)
            self.erase(i, j - 1, grid)
            self.erase(i, j + 1, grid)


# grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"],
# ]
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

print(Solution().numIslands(grid))
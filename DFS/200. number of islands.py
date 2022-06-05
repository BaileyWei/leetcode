class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.r, self.c = len(grid), len(grid[0])
        self.grid = grid
        count = 0
        for i in range(self.r):
            for j in range(self.c):
                if self.grid[i][j] == '1':
                    # 找到一个岛，将周围连通岛都设为0，记为一个岛屿
                    self.dfs(i, j)
                    count += 1
        return count

    def dfs(self, i, j):
        if not 0 <= i < self.r or not 0 <= j < self.c or self.grid[i][j] == '0':
            return
        # 设置为0防止重复计算
        self.grid[i][j] = '0'
        # 将相连的所有岛都设为0
        self.dfs(i+1, j)
        self.dfs(i-1, j)
        self.dfs(i, j+1)
        self.dfs(i, j-1)
if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]


    Solution().numIslands(grid)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        n_rows, n_cols = len(grid), len(grid[0])

        def dfs(i: int, j: int):
            if i < 0 or i >= n_rows or j < 0 or j >= n_cols or not grid[i][j]:
                return 0

            grid[i][j] = 0
            return 1 + dfs(i, j-1) + dfs(i,j+1) + dfs(i-1, j) + dfs(i+1, j)

        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j]:
                    res = max(res, dfs(i, j))

        return res
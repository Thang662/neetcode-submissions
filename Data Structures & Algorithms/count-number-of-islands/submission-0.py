class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        n_rows, n_cols = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= n_rows or j < 0 or j >= n_cols or grid[i][j] != '1':
                return

            grid[i][j] = '0'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res
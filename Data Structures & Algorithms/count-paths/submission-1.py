class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]

            if i == m - 1 and j == n - 1:
                return 1

            if i == m or j == n:
                return 0

            res = dfs(i + 1, j)
            res += dfs(i, j + 1)
            memo[(i, j)] = res

            return res

        return dfs(0, 0)
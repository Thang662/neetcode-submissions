class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i: int, j: int) -> int:
            if j >= len(prices):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] =  max(prices[j] - prices[i] + dfs(j+2, j+3), dfs(i, j+1), dfs(i+1, j+1))
            return memo[(i, j)]
        return dfs(0, 1)
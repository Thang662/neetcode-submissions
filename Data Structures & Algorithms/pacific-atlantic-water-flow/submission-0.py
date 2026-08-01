class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n_rows, n_cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(i: int, j: int, visited: Set[Tuple[int, int]], prev_height: int) -> None:
            if min(i, j) < 0 or i == n_rows or j == n_cols or (i, j) in visited or heights[i][j] < prev_height:
                return
            
            visited.add((i, j))
            dfs(i+1, j, visited, heights[i][j])
            dfs(i-1, j, visited, heights[i][j])
            dfs(i, j+1, visited, heights[i][j])
            dfs(i, j-1, visited, heights[i][j])

        for i in range(n_cols):
            dfs(0, i, pac, heights[0][i])
            dfs(n_rows-1, i, atl, heights[n_rows-1][i])
        
        for i in range(n_rows):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, n_cols-1, atl, heights[i][n_cols-1])

        res = []
        for i in range(n_rows):
            for j in range(n_cols):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res
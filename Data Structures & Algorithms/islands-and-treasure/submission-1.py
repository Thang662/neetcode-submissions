from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = set()
        n_rows, n_cols = len(grid), len(grid[0])

        def add_cell(i: int, j: int) -> None:
            if min(i, j) < 0 or i == n_rows or j == n_cols or (i, j) in visited or grid[i][j] == -1:
                return 

            queue.append((i, j))
            visited.add((i, j))

        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                grid[i][j] = dist

                add_cell(i+1, j)
                add_cell(i-1, j)
                add_cell(i, j+1)
                add_cell(i, j-1)
            dist += 1        
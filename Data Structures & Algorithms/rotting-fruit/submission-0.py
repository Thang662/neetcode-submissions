from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        visited = set()
        queue = deque()
        n_rows, n_cols = len(grid), len(grid[0])

        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))
                    flag = True
                elif grid[i][j] == 1:
                    fresh += 1
        
        
        def add_cell(i: int, j: int) -> None:
            nonlocal fresh
            if min(i, j) < 0 or i == n_rows or j == n_cols or (i, j) in visited or not grid[i][j]:
                return

            if grid[i][j] == 1:
                fresh -= 1
            visited.add((i, j))
            queue.append((i, j))

        res = -1 if queue else 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                add_cell(i+1, j)
                add_cell(i-1, j)
                add_cell(i, j+1)
                add_cell(i, j-1)
            res += 1

        return res if not fresh else -1
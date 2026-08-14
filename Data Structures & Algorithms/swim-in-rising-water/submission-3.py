import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        heap = []
        heapq.heappush(heap, (grid[0][0], abs(- n_rows + 1) + abs(- n_cols + 1), (0, 0)))
        visited = set()

        def add_cell(x: int, y: int, level: int) -> None:
            if min(x, y) < 0 or x == n_rows or y == n_cols or (x, y) in visited:
                return
            heapq.heappush(heap, (max(level, grid[x][y]), abs(x - n_rows + 1) + abs(y - n_cols + 1), (x, y)))

        while heap:
            level, dist, (x, y) = heapq.heappop(heap)
            visited.add((x, y))

            if not dist:
                return level

            add_cell(x + 1, y, level)
            add_cell(x - 1, y, level)
            add_cell(x, y + 1, level)
            add_cell(x, y - 1, level)

            # print(heap)

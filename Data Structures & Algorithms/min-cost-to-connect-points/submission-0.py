import heapq
from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = defaultdict(list)
        res = {}
        visited = set()
        heap = []
        idx2point = {i: (x, y) for i, (x, y) in enumerate(points)}
        print(idx2point)

        heapq.heappush(heap, (0, 0))

        while heap:
            w1, n = heapq.heappop(heap)
            res[n] = min(w1, res.get(n, w1))
            if n in visited:
                continue
            
            visited.add(n)

            for i, (x2, y2) in enumerate(points):
                if i not in visited:
                    x1, y1 = idx2point[n]
                    heapq.heappush(heap, (abs(x2 - x1) + abs(y2-y1), i))
            # print(heap, res)
        return sum(res.values())

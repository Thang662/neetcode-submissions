import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for point in points:
            heapq.heappush(res, (-point[0] ** 2 - point[1] ** 2, point))
            if len(res) > k:
                heapq.heappop(res)

        return [x[1] for x in res]
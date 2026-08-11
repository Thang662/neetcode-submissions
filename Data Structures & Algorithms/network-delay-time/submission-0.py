class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Bellman Ford
        res = [float('inf') for i in range(n)]
        res[k-1] = 0

        for _ in range(n):
            for a, b, w in times:
                if res[a-1] != float('inf'):
                    res[b-1] = min(res[b-1], res[a-1] + w)
        return max(res) if max(res) != float('inf') else -1
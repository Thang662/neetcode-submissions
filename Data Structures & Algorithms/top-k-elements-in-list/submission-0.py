import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        res = []
        for num, count in freqs.items():
            heapq.heappush(res, (count, num))

            if len(res) > k:
                heapq.heappop(res)

        return [num for count, num in res]
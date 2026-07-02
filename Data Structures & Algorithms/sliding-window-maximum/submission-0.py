import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        # heap
        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))

            if i >= k - 1:
                while i - k >= heap[0][1]:
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res
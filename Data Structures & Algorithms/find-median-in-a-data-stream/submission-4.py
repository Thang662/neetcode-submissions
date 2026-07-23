import heapq
class MedianFinder:

    def __init__(self): 
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # if not self.min_heap:
        #     heapq.heappush(self.min_heap, num)

        heapq.heappush(self.min_heap, num)

        if len(self.min_heap) - 1 > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        if self.max_heap and -self.max_heap[0] > self.min_heap[0]:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        print(self.min_heap, self.max_heap)
    def findMedian(self) -> float:
        return self.min_heap[0] if (len(self.min_heap) + len(self.max_heap)) % 2 else (self.min_heap[0] - self.max_heap[0]) / 2
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian() 
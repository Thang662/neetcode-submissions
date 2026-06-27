import heapq
class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []        

    def addNum(self, num: int) -> None:
        if self.minheap and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush_max(self.maxheap, num)

        if len(self.maxheap) - len(self.minheap) > 1:
            num = heapq.heappop_max(self.maxheap)
            heapq.heappush(self.minheap, num)
        
        if len(self.minheap) - len(self.maxheap) > 1:
            num = heapq.heappop(self.minheap)
            heapq.heappush_max(self.maxheap, num)


    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        return (self.maxheap[0] + self.minheap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
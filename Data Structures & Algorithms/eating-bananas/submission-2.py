class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = float('inf')
        # self solution, not optimized
        while l <= r:
            mid = l + (r - l) // 2
            time = sum([(pile - 1) // mid + 1 for pile in piles])
            if time > h:
                l = mid + 1
            elif time <= h:
                r = mid - 1
                res = min(res, mid)
        return res            
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        # self solution, not optimized
        while l <= r:
            mid = l + (r - l) // 2
            time = sum([(pile - 1) // mid + 1 for pile in piles])
            if time > h:
                l = mid + 1
            else:
                r = mid - 1
                res = mid
        return res            
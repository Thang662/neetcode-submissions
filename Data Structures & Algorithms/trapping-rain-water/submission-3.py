class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0

        # Pointers
        while l < r:
            if maxL > maxR:
                r -= 1
                maxR = max(maxR, height[r])
                res += max(0, maxR - height[r])
            else:
                l += 1
                maxL = max(maxL, height[l])
                res += max(0, maxL - height[l])
        return res
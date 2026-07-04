class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        # Remember the pattern: can only expand if next height is greater or equal --> monotonic stack
        for i in range(len(heights) + 1):
            while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
                idx = stack.pop()
                w = i if not stack else i - stack[-1] - 1
                h = heights[idx]
                res = max(res, w * h)
            stack.append(i)
        return res
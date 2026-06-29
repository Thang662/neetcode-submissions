class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0

        # stack
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                mid = stack.pop()
                if stack:
                    l = stack[-1]
                    h = min(height[l], height[i]) - height[mid]
                    res += h * (i - l - 1)
            stack.append(i)
        return res
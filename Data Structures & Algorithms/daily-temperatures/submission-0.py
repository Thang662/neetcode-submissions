class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, idx = stack.pop()
                res[idx] = i - idx
            stack.append((temp, i))

        return res
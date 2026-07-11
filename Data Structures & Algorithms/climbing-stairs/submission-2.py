class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        a, b = 1, 2

        for i in range(n-2):
            a, b = b, a+b
        return b
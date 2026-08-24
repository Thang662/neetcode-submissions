class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            num = 0
            while n:
                num += (n % 10) ** 2
                n //= 10
            n = num
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
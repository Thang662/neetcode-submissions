class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        maxlen = 0
        n = len(s)
        dp = [[False] * n for i in range(n)]

        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and (i - j < 3 or dp[i-1][j+1]):
                    dp[i][j] = True
                    if i - j + 1 > maxlen:
                        maxlen = i - j + 1
                        res = s[j:i+1]
        return res
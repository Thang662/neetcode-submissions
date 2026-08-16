class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        n = len(s)
        def dfs(i: int) -> int:
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            
            res = dfs(i+1)

            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and "0" <= s[i+1] < "7")):
                res += dfs(i+2)
            dp[i] = res
            return res

        res = dfs(0)
        return res 

            
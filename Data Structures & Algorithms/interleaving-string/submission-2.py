class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3: return True
        if len(s1) + len(s2) > len(s3): return False
        memo = {}
        def dfs(i: int, j: int, cur: int) -> bool:
            if i == len(s1) or j == len(s2):
                return False

            if (i, j) in memo:
                return memo[(i, j)]
            c = s2[j] if cur else s1[i]
            # print(i, j, cur, c, s3[i+j+1], memo)

            if c != s3[i+j+1]:
                # print('haha')
                return False
            
            if (i + j + 2) == len(s3):
                return True
            memo[(i, j)] = dfs(i+1, j, 0) or dfs(i, j+1, 1)
            return memo[(i, j)]
        res1 = dfs(0, -1, 0)
        # print('first')
        res2 = dfs(-1, 0, 1)
        return res1 or res2
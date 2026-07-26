class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i: int, j: int, path: list[str]) -> None:
            # if not self.isPali(s, i, j): return 
            if j == len(s):
                if self.isPali(s, i, j-1):
                    path.append(s[i:j])
                    res.append(path[:])
                    path.pop()
                return

            if self.isPali(s, i, j-1):
                path.append(s[i:j])
                dfs(j, j+1, path)
                path.pop()
            dfs(i, j+1, path)
        dfs(0, 1, [])
        # print(res)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
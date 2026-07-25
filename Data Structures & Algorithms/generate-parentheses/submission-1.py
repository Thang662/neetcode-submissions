class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(x: int, y: int, path = list[str]) -> None:
            if not x and not y:
                res.append(''.join(path))

            if x:
                path.append('(')
                dfs(x-1, y, path)
                path.pop()
            if y > x:
                path.append(')')
                dfs(x, y-1, path)
                path.pop()
        dfs(n, n, [])
        return res
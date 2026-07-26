class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        d2l = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []
        def dfs(i: int, path: list[str]) -> None:
            if i == len(digits):
                res.append(''.join(path))
                return

            for l in d2l[digits[i]]:
                path.append(l)
                dfs(i+1, path)
                path.pop()

        dfs(0, [])
        return res
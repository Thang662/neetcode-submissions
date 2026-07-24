class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(start: int, remaining: int, path: list[int]):
            if remaining < 0: return
            print(path, start)
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if (i > start) and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                dfs(i + 1, remaining - candidates[i], path)
                path.pop()                
                # dfs(i + 1, remaining, path)
        dfs(0, target, [])
        return res
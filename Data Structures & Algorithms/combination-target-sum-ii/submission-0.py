class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if num > remaining:
                    break

                if i > start and num == candidates[i - 1]:
                    continue

                path.append(num)
                backtrack(i + 1, remaining - num)
                path.pop()

        backtrack(0, target)
        return res
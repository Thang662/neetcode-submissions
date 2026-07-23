class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i: int, remaining: int) -> None:
            if remaining < 0 or i == len(nums): return
            if remaining == 0:
                res.append(path[:])
                return

            path.append(nums[i])
            dfs(i, remaining - nums[i])
            path.pop()
            dfs(i+1, remaining)

        dfs(0, target)
        return res
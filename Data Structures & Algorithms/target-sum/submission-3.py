class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = []
        n = len(nums)
        path = []

        def dfs(i, remaining):
            # print(path, remaining)
            if i == n:
                if remaining == 0:
                    res.append(path[:])
                return

            path.append(nums[i])
            dfs(i+1, remaining-nums[i])
            path.pop()

            path.append(-nums[i])
            dfs(i+1, remaining+nums[i])
            path.pop()

        dfs(0, target)
        # print(res)
        return len(res)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        dp = {}
        # naive approach
        def dfs(i: int, remaining: int) -> bool:
            if remaining == 0:
                return True
            if i == len(nums):
                return False 

            if (i, remaining) in dp:
                return dp[i, remaining]


            dp[(i, remaining)] = dfs(i+1, remaining) or dfs(i+1, remaining - nums[i])

            return dp[(i, remaining)]
        return dfs(0, total/2)
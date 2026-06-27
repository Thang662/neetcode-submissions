class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i, target):
            if target == 0:
                res.append(path[:])
                return

            if target < 0 or i == len(nums):
                return

            path.append(nums[i])
            backtrack(i, target - nums[i])
            path.pop()

            backtrack(i + 1, target)

        backtrack(0, target)
        return res
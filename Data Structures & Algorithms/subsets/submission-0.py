class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(nums, i):
            nonlocal path

            if i == len(nums):
                res.append([*path])
                return

            backtrack(nums, i + 1)

            path.append(nums[i])
            backtrack(nums, i + 1)
            path.pop()

        backtrack(nums, 0)
        return res                
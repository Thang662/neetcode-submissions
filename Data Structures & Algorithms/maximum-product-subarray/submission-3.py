class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        suffix = prefix = 0
        res = nums[0]
        n = len(nums)

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n-i-1] * (suffix or 1)
            res = max(res, prefix, suffix)
        return res
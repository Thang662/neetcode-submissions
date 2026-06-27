class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        res = 0
        for x in nums:
            if x - 1 not in nums:
                y = x
                while y in nums:
                    y += 1
                res = max(res, y - x)
        return res
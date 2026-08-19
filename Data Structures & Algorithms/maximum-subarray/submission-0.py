class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        tmp = 0
        for num in nums:
            tmp += num
            res = max(res, tmp)
            if tmp < 0:
                tmp = 0
        return res
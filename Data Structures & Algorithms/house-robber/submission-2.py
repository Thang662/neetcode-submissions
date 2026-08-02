class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, nums[0]

        for i in range(1, len(nums)):
            a, b = b, max(b, a + nums[i])
        return b
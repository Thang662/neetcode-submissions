class Solution:
    def rob(self, nums: List[int]) -> int:
        # res[i] = max(res[i-1], res[i-2] + nums[i])
        # but n-1 and 0 are adjacent
        a, b = 0, 0
        for i in range(1, len(nums)):
            a, b = b, max(b, a + nums[i])

        c, d = 0, 0
        for i in range(len(nums)-1):
            c, d = d, max(d, c + nums[i])
        return max(b, d, nums[0])
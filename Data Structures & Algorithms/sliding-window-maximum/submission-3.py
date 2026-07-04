from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for i in range(len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()

            q.append(i)

            if i - k >= q[0]:
                q.popleft()

            if i + 1 >= k:
                res.append(nums[q[0]])
        return res
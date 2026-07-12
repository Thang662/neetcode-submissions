class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        while fast:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return fast

        return slow
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')

        # the smallest (pivot point) (if the array is rotated) is always on the sorted right side
        # --> we want to move the mid point to right side and narrow left and right pointers
        # when mid = pivot point --> r = mid - 1, r is on left side and update till < l but still got the pivot
        # the process is just go through every point and check if it's min or not --> final min will be pivot point
        # if l and r on the same side --> go through pivot point also work when the array is not rotated
        # How do we find pivot point without tracking
        while l <= r:
            if nums[l] < nums[r]: # on the same side
                res = min(res, nums[l])
                break
            
            mid = l + (r - l) // 2
            if nums[mid] >= nums[l]: # mid on the sorted left side
                l = mid + 1
            else: # mid on the sorted right side
                r = mid - 1

            res = min(res, nums[mid])
        return res
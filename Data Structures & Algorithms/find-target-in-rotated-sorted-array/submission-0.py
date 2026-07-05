class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        # self thinking
        while l <= r:
            mid = l + (r - l) // 2
            print(f'Before: {l, mid, r}')
            if target == nums[mid]:
                return mid

            # mid on the left side
            if nums[mid] > nums[r]:
                print('Left side')
                # target in the left side
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            # mid on the right side
            else:
                print('Right side')
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            print(l, mid, r)
        return -1
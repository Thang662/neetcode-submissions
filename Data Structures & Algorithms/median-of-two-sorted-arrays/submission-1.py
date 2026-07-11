class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        half = (m + n) // 2
        
        # scan on smaller array --> half - i always < n
        if m > n:
            m, n = n, m
            nums1, nums2 = nums2, nums1
        
        l, r = 0, m - 1
        count = 0
        while True:
            i = l + (r - l) // 2
            j = half - i - 2
            print(i, j, m, n)
            
            a_left = nums1[i] if i >= 0 else float('-inf')
            print(f'a_left: {a_left}')

            a_right = nums1[i+1] if i + 1 < m else float('inf')
            print(f'a_right: {a_right}')

            b_left = nums2[j] if j >= 0 else float('-inf')
            print(f'b_left: {b_left}')

            b_right = nums2[j+1] if j + 1 < n else float('inf')
            print(f'b_right: {b_right}') 

            if a_right < b_left:
                l = i + 1
            elif a_left > b_right:
                r = i - 1
            else:
                print('haha')
                if (m + n) % 2:
                    print('hi')
                    return min(a_right, b_right)
                else:
                    print('h')
                    return (min(a_right, b_right) + max(a_left, b_left)) / 2
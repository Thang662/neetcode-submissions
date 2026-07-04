class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) * len(matrix) - 1

        # Own solution, not optimized
        while l <= r:
            mid = l + (r - l) // 2
            row, col = mid // len(matrix[0]), mid % len(matrix[0])
            if matrix[row][col] > target:
                r = mid - 1
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                return True
        return False
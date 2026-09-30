class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_low, row_high = 0, len(matrix) - 1
        row = -1

        while row_low <= row_high:
            row_mid = (row_low + row_high) // 2

            if matrix[row_mid][0] <= target <= matrix[row_mid][-1]:
                row = row_mid
                break
        
            elif target < matrix[row_mid][0]:
                row_high = row_mid - 1
            
            else:
                row_low = row_mid + 1

        else: return False
        
        low, high = 0, len(matrix[row]) - 1

        while low <= high:
            mid = (low + high) // 2

            if matrix[row][mid] == target:
                return True

            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
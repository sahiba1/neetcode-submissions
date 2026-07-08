class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        
        low , high = 0 , rows * cols - 1
        while low<=high:
            mid = (low + high)//2
            row = mid // cols
            col = mid % cols
            if target < matrix[row][col]:
                high = mid - 1
            elif target > matrix[row][col]:
                low = mid + 1

            else:
                return True
        return False

        
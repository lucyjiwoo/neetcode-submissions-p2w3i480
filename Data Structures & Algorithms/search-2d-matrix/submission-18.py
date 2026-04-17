class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        COLS = len(matrix[0])
        l,r = 0, len(matrix) * COLS - 1
        while l < r:
            mid = (l+r)//2
            row = mid // COLS
            col = mid % COLS
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                r = mid
        if target == matrix[l//COLS][l%COLS]:
            return True
        return False
            

        
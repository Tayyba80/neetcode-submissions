class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW , COL = len(matrix) , len(matrix[0])

        l , r = 0 , (ROW * COL) -1
        
        while l <= r:
            mid = l + ((r-l) // 2)
            row , col = mid // COL , mid % COL # maps our flattend array index to real 2d array row,col, if we divide mid by cols we get the row number and if we take mod we get the column so for 12 we will get [1][2]
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid -1
        return False
            

        
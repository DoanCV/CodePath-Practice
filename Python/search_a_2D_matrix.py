"""
the elements in each row are sorted in ascending order and the elements in the row below is greater than the elements in the current row

since this is true we can use binary search, we just have to be careful on how to deal with different rows
    we can convert 2D array to 1D array literally or by position

n * m matrix convert to an array => matrix[x][y] => a[x * m + y]

an array convert to n * m matrix => a[x] => matrix[x / m][x % m]
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # constraints suggest that we do not need to check for empty array
        
        
        n = len(matrix) # rows
        m = len(matrix[0]) # columns
        
        start = 0
        end = n * m - 1
        
        while start <= end:
            
            mid = (start + end) // 2
            
            if matrix[mid // m][mid % m] == target:
                return True
            
            elif matrix[mid // m][mid % m] < target:
                start = mid + 1
            
            else:
                end = mid - 1
                
                
        return False

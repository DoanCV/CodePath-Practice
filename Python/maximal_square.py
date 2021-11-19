"""
We can store the max side length for each square starting from the bottom right corner
    each index will peek to the right, down and downright to see if a square is possible
        this way we do not repeat work
    m does not have to equal n

O(m * n) time complexity where m and n are the dimensions of the given matrix. We compute values for each position once.
O(m * n) space complexity since we have a cache in the form of a hashmap with the row and column as the key
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        num_rows, num_columns = len(matrix), len(matrix[0])
        cache = {}
        
        def helper(row, column):
            if row >= num_rows or column >= num_columns:
                return 0
            
            if (row, column) not in cache:
                down = helper(row + 1, column)
                right = helper(row, column + 1)
                diagonal = helper(row + 1, column + 1)
                
                # if the value at the current row and column is 0 then we do nothing since we cant make a square with this top left corner
                cache[(row, column)] = 0 
                if matrix[row][column] == "1":
                    cache[(row, column)] = 1 + min(down, right, diagonal)
            
            return cache[(row, column)]
                
        
        helper(0,0)
        return max(cache.values()) ** 2

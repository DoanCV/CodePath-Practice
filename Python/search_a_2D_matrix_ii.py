"""
U
We are given a 2d matrix of integers
    integers in each row are sorted in ascending order from left to right
    integers in each column are sorted in ascending from top to bottom

find the target, return True if it exists in the matrix else return False


M/P
we want to reduce as much of the search space as possible with each step
    search from the top-right element and reduce the search space by one row or column at each step

in the given example 
[
    [1, 4, 7, 11,15],
    [2, 5, 8, 12,19],
    [3, 6, 9, 16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
]
where target = 12

we compare 12 and 15, ie the top right element
    12 < 15 so we know that 12 cant be in the last column since columns are sorted in ascending order
then we compare 12 and 11, ie the element to the left of 15
    12 > 11 so we know that 12 cant be in the row with 11 since rows are sorted in ascending order

since everything is increasing and not nondecreasing we know there are no duplicates

E
O(N + M) time complexity where N is the number of rows in the matrix and M is the number of columns in the matrix. We cut down a row or column at each step. In the worst case we cut down every row and column. We do not visit every element.
O(1) space complexity since we solve in place.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        
        row = 0
        column = len(matrix[0]) - 1
        
        while column >= 0 and row < len(matrix):
            
            if target == matrix[row][column]:
                return True
            elif target < matrix[row][column]:
                column -= 1
            else:
                row += 1
                
        return False

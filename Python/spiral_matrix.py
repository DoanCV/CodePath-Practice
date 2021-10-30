"""
a walk through of example given

[[1,2,3,4],
[5,6,7,8],
[9,10,11,12]]
answer_expected = [1,2,3,4,8,12,11,10,9,5,6,7]

we start with the following boundaries
rowBegin = 0
rowEnd = len(matrix) - 1 = 2
columnBegin = 0 
columnEnd = len(matrix[0]) - 1 = 3

no overlap yet so we go into while loop

from the first for loop (going right)
result = [1,2,3]

from the second for loop (going down)
result = [1,2,3,4,8]

from the third for loop (going left)
result = [1,2,3,4,8,12,11,10]

from the fourth for loop (going up)
result = [1,2,3,4,8,12,11,10,9,5]

update boundaries
rowBegin = 1
rowEnd = 1
columnBegin = 1
columnEnd = 2

we cant enter the while loop again but we are not done
    this is becuase if N == M then we have the middle element left
    if N != M that means we have a subrow or subcolumn left
        the size of this subarray will be determined by our boundaries
    both of these cases means we have an overlap in the boundary
        if it is just the middle element then the left and right are equal and so are the top and bottom
            otherwise one of the two pairs of boundaries are not equal
                we can loop through both rows and columns but by default one will be held constant

O(N * M) time complexity where N is the number of rows and M is the number of columns in the given matriz. We visit each element once
O(N * M) space complexity for our output since there are N * M elements
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        if len(matrix) == 0:
            return result
        
        # four boundaries are donated by start and end indicies
        rowBegin = 0
        rowEnd = len(matrix) - 1
        columnBegin = 0
        columnEnd = len(matrix[0]) - 1
        
        # while our walls have not crossed
            # go right, then down, then left, then up
            # repeat but with new boundaries
        while rowBegin < rowEnd and columnBegin < columnEnd:
            
            # go right
            for i in range(columnBegin, columnEnd):
                result.append(matrix[rowBegin][i])
            
            # go down 
            for i in range(rowBegin, rowEnd):
                result.append(matrix[i][columnEnd])
            
            # go left
            for i in range(columnEnd, columnBegin, -1):
                result.append(matrix[rowEnd][i])
            
            # go up
            for i in range(rowEnd, rowBegin, -1):
                result.append(matrix[i][columnBegin])
            
            # set up for the next iteration
            rowBegin += 1
            columnEnd -= 1
            columnBegin += 1
            rowEnd -= 1
        
        # check the reaminaing 1xM or NX1 submatrix
        if len(result) < len(matrix) * len(matrix[0]):
            for row in range(rowBegin, rowEnd + 1):
                for col in range(columnBegin, columnEnd + 1):
                    result.append(matrix[row][col])
        
        return result

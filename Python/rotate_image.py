class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # reverse the rows
        left = 0
        right = len(matrix) - 1
        
        while left < right:
            matrix[left], matrix[right] = matrix[right], matrix[left]
            
            left += 1
            right -= 1
        
        # transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        return matrix

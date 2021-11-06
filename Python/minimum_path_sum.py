"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path. Return the path sum not the actual path

Note: You can only move either down or right at any point in time.


Bottom Up DP
    we can only go down or right (staying in the bounds)
    knowing this we can store the minimum path values
        first fill out the base cases which is the top row and leftmost column

"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        columns = len(grid[0])
        
        # fill base case path row
        for j in range(1, columns):
            grid[0][j] += grid[0][j - 1]
            
        # fill base case path column
        for i in range(1, rows):
            grid[i][0] += grid[i - 1][0]
        
        # build the rest
        for i in range(1, rows):
            for j in range(1, columns):
                grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        
        
        return grid[-1][-1]

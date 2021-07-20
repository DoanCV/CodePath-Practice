class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        DFS
        Loop through the rows and columns of the 2D matrix
        When we hit a 1 we send a search party to neighbors
        We sink the current index and continue until we hit all the connections
        All of that makes one island
        """
        
        count = 0
        
        if len(grid) == 0:
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        
        return count
    
    
    def dfs(self, grid, row, column):
        
        # out of bounds
            # outside the matrix, or the current index is not an island so there is no connection
        if (row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]) or grid[row][column] != "1"):
            return
    
        grid[row][column] = 0
        
        self.dfs(grid, row + 1, column)
        self.dfs(grid, row - 1, column)
        self.dfs(grid, row, column + 1)
        self.dfs(grid, row, column - 1)

# O(N * M) time complexity, where N is the number of rows and M is the number of columns in the given matrix. We have to traverse through the entire matrix to check for islands.
# O(1) space complexity, since we are not using any extra data structures.

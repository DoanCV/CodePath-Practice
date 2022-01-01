class Solution:
    def cherryPickup(self, grid):
        self.memo = {}
        cherries = self.dfs(grid, 0, 0, 0, len(grid[0]) - 1) # start with top left and top right
        return max(cherries, 0)
    
    
    def dfs(self, grid, x1, y1, x2, y2):
        # state has already been computed
        if (x1, y1, x2, y2) in self.memo:
            return self.memo[(x1, y1, x2, y2)]
        
        # out of bounds, we dont need to check for -x since we can only go down
        if y1 < 0 or y2 < 0 or y1 > len(grid[0]) - 1 or y2 > len(grid[0]) - 1:
            return float("-inf")
        
        # we hit the bottom
        if x1 == len(grid) or x2 == len(grid):
            return 0
        
        """
        # try all 9 directions
        d1 = self.dfs(grid, x1 + 1, y1 - 1, x2 + 1, y2 - 1)     # 1: down left, 2: down left
        d2 = self.dfs(grid, x1 + 1, y1 - 1, x2 + 1, y2)         # 1: down left, 2: down
        d3 = self.dfs(grid, x1 + 1, y1 - 1, x2 + 1, y2 + 1)     # 1: down left, 2: down right
        d4 = self.dfs(grid, x1 + 1, y1, x2 + 1, y2 - 1)         # 1: down, 2: down left
        d5 = self.dfs(grid, x1 + 1, y1, x2 + 1, y2)             # 1: down, 2: down
        d6 = self.dfs(grid, x1 + 1, y1, x2 + 1, y2 + 1)         # 1: down, 2: down right
        d7 = self.dfs(grid, x1 + 1, y1 + 1, x2 + 1, y2 - 1)     # 1: down right, 2: down left
        d8 = self.dfs(grid, x1 + 1, y1 + 1, x2 + 1, y2)         # 1: down right, 2: down
        d9 = self.dfs(grid, x1 + 1, y1 + 1, x2 + 1, y2 + 1)     # 1: down right, 2: down right

        max_result = max([d1,d2,d3,d4,d5,d6,d7,d8,d9])
        """
        
        # two for loops is more concise
        max_result = 0
        for dx1, dy1 in ((1,0), (1,-1), (1,1)):
            for dx2, dy2 in ((1,0), (1,-1), (1,1)):
                max_result = max(max_result, self.dfs(grid, x1 + dx1, y1 + dy1, x2 + dx2, y2 + dy2))
        
        # if the two robots are on the same place then only one can pick up the cherries
        if x1 == x2 and y1 == y2:
            result = max_result + grid[x1][y1]
        else:
            result = max_result + grid[x1][y1] + grid[x2][y2]
        
        self.memo[(x1, y1, x2, y2)] = result # cache state
        
        return result

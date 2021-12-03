"""
Find the number of distinct islands
  an island is a group of 1s connected vertically and horizontally
  islands are distinct based on their shape/structure

Thing is when we DFS the way we dfs is consistent for the same shapes
  So if we encode a DFS path and store in a set only unique island shapes will end up in the set
  the encoding should use:
  X = start   
  O = water or out of bounds      
  U = up
  R = right 
  L = left 
  D = down

The DFS itself is the same as number of islands where we flip 1s to 0s but we build a path on top of that
"""

def num_of_distinct_islands(grid):
  if grid is None: 
    return 0


  shapes = set()
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == "1":
        path = helper(grid, i, j, "X")
        shapes.add(path)

  return len(shapes)

def helper(grid, row, column, direction):
  if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]) or grid[row][column] == 0:
    return "O"

  grid[row][column] = 0

  left = helper(grid, row, column - 1, "U")
  right = helper(grid, row, column + 1, "R")
  up = helper(grid, row - 1, column, "U")
  down = helper(grid, row + 1, column, "D")

  return direction + left + right + up + down

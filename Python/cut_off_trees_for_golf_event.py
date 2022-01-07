"""
U
There are trees in a forest represented as a matrix
    0 means we can't walk on the cell
    1 means an empty cell that we can walk on
    greater than 1 means we can wlak thorugh and it is the tree's height 

We start at (0,0) and can move north, east, south, and west
    if you are on a cell with a tree we can cut it off
    we must cut off the trees from shortest to tallest
    Note that you can cut off the first tree at (0, 0) before making any steps

Find the minimum number of steps to cut off all the trees
    If you can't cut off the trees, return -1


M
BFS

P
Get all the trees in sorted order 

We use BFS to try out the paths and count the number of steps it takes from the previous node
    if steps < 0 then we are unable to move further due to obstacle so return -1 else add these steps to the totalSteps
    keep a visited set


"""
from collections import deque
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        row_count = len(forest)
        column_count = len(forest[0])
        
        forest_trees = [(forest[i][j], i, j) for i in range(row_count) for j in range(column_count) if forest[i][j] > 1]
        forest_trees.sort()
        
        def bfs(row, column, tree_x, tree_y):
            
            visited = [[False for _ in range(column_count)] for _ in range(row_count)]
            
            queue = deque()
            queue.append( (row, column, 0) )
            
            while queue:
                curr_x, curr_y, curr_steps = queue.popleft()
                
                if curr_x == tree_x and curr_y == tree_y:
                    return curr_steps
                
                for x, y in [(curr_x - 1, curr_y), (curr_x + 1, curr_y), (curr_x, curr_y - 1), (curr_x, curr_y + 1)]:
                    if x >= 0 and x < row_count and y >= 0 and y < column_count and forest[x][y] > 0 and not visited[x][y]:
                        visited[x][y] = True
                        queue.append( (x, y, curr_steps + 1) )
            
            return -1
        
        x = 0
        y = 0
        total_steps = 0
        for tree in forest_trees:
            steps = bfs(x, y, tree[1], tree[2])
            
            if steps < 0:
                return -1
            
            total_steps += steps
            x = tree[1]
            y = tree[2]
        
        return total_steps   

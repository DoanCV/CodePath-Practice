"""
0 is empty cell
1 is a fresh orange
2 is a rotten orange

graph terminology version
    orange is a node
    distance from rotten to fresh is a level and is also the time it takes in minutes to spoil if there are no other rotten oranges
    the infection spreads in four directions, up, down, left, right so that means each level can have at most 4 nodes

we want to find the furthest distance a rotten orange is from a fresh one since that is the minimum number of mintues to spoil all the oranges

we can dfs from the rotten oranges
    but it seems like we can have multiple rotten oranges 
        that means multiple oranges can cover more fresh oranges sooner than just 1 based on the starting positions

instead we can bfs since we are looking for distances which is a level at a time
    we will do this iteratively with a queue of rotten oranges
    keep track of the level
    
    


get the number of fresh oranges and then add rotten oranges to a queue
    queue will hold the position of rotten oranges

for each level check all four directions
    if there is a fresh next to the rotten 
        add that fresh one to the queue which would mean it spoiled
        increment the level and decrement the fresh orange count

O(row * column) time complexity since we start by traversing throuhg the entire grid to count the fresh oranges and add the rotten ones to out queue. That is the most expensive part of our algorithm.
O(row * column) space complexity since in the worst case we have all rotten oranges so our queue will hold them all.
"""
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh_orange_count = 0
        queue = deque()
        
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                
                if grid[row][column] == 2:
                    queue.append( (row, column) )
                elif grid[row][column] == 1:
                    fresh_orange_count += 1
        
        # encode 4 directions as changes in x,y position
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        level_minutes = 0
        
        # BFS
        # continue if there are still rotten oranges and if there are still fresh oranges
        while queue and fresh_orange_count > 0:
            
            # increment the level
            level_minutes += 1
            
            
            # loop through each element of the level
            level_length = len(queue)
            for _ in range(level_length):
                
                row, column = queue.popleft()
                
                for x, y in directions:
                
                    # if we are out of bounds then ignore and continue
                    # if we have a 0 or a 2 ignore and continue since the orange is already rotten and empty space cant be rotten
                    new_row = row + x
                    new_column = column + y
                    if new_row < 0 or new_row > len(grid) - 1 or new_column < 0 or new_column > len(grid[0]) - 1 or grid[new_row][new_column] != 1:
                        continue
                    else:
                        fresh_orange_count -= 1
                        grid[new_row][new_column] = 2
                        queue.append( (new_row, new_column) )                        
        
        # we have a case where there were never any rotten oranges in the first place, meaning level is still 0, so return 0
        # if there are still fresh oranges after accounting for all of the rotten spread then return -1
        if fresh_orange_count > 0:
            return -1
        else:
            return max(level_minutes, 0)

"""
U
We have a wall of bricks
    The bricks have the same height but they may not always have the same width
    each row of bricks all add up to the same total width

We need to draw a line from top to bottom and minimize the number of bricks that it goes through
    we cant draw a line on the sides of the leftmost and rightmost bricks since that never crosses a brick and is trivial
    
    
M
avoiding a brick means going in between two bricks which is essentially an edge
    if we maximize the number of edges across all possible lines then that means we found the minimum bricks crossed
    the number of rows minus the frequency of edges is our answer
    
we can find the position of every edge for every level
    paths are vertical so if an edge exists in the same horizontal position then it is part of the same line that we draw

edge case:
    we have have no edges apart from beyond the leftmost side and rightmost side so we have to cross bricks for every row
    this will occur when we have the a single width brick at each level with the same width
        if we have more than 1 brick at each level then there is always going to be an edge
        our answer here is the number of rows/levels in our wall
    
P
we need to keep track of the max amount of edges, start with 0 since we havent found any edges
we have a frequency map of each edge position from 0 to the total width of the wall

we loop through each row of the wall

    for each brick we use the width to find our edge position since each edge in a level is separated by just brick width
    
    then we have to update our max edge count

return number of rows/levels - max edge count

I
See class below

R
Another edge case:
    if we have really large width bricks it is not worth intializing our hashmap like the way I commented out since that makes a key for each position
    if we find an edge position then we make a key otherwise don't bother

E
O(N * M) time complexity, where N is the number of rows/levels in our wall and M is the number of bricks at each level. We have to check every brick for edges and we do this with a nested for loop.
O(M) space complexity since our hashmap stores a key for each edge position. The worst case number of keys is equal to the total width of any level - 1. We subtract 1 since we do not include the rightmost edge since that is the trivial result.

"""
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        max_edges = 0
        number_of_rows = len(wall)
                
        """
        # find the width of the wall
        # very inefficient since we add a key for every position even though there may not be an edge
        total_width = 0
        for i in range(len(wall[0])):
            total_width += wall[0][i]
            
        position_map = {i : 0 for i in range(1, total_width)}
        """
        
        position_map = {}
        
        for row in range(number_of_rows):
            
            edge_position = 0
            
            # skip the last brick's right edge
            for brick in range(len(wall[row]) - 1):
                
                edge_position += wall[row][brick]
                
                # if this is our first time seeing an edge at the current position, add the key
                if edge_position not in position_map:
                    position_map[edge_position] = 0
                
                position_map[edge_position] += 1
                
                max_edges = max(max_edges, position_map[edge_position])
        
        return number_of_rows - max_edges

"""
Key point: there are only 2 islands 
        
Two approaches
    1. find both islands, store all the points inside each island. then calculate the distance between all the points, return the minimum
    2. find first island in its entirety with dfs then bfs outwards while keeping track of steps taken until we find the first element of the other island
"""

from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        def isOutOfBounds(x, y):
            return (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]))

        def dfs(row, column):
            if grid[row][column] == 1:
                queue.append( [row, column, 0] ) # we can add all elements of the first island and still have the correct distance since the border elements will hit the other island first. remember one step at a time so inner ones wait their turn in the bfs queue

                grid[row][column] = "munch"
                for dx, dy in directions:
                    x = row + dx
                    y = column + dy
                    if not isOutOfBounds(x,y):
                        dfs(x, y)
        
        def bfs():
            visited = set()
            while queue:
                row, column, distance = queue.popleft()
                if grid[row][column] == 1:
                    return distance - 1
                else:
                    for dx, dy in directions:
                        x = row + dx
                        y = column + dy
                        if not isOutOfBounds(x,y) and (x, y) not in visited:
                            visited.add( (x,y) )
                            queue.append( [x, y, distance + 1] )

        queue = deque()
        foundFirstIsland = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    foundFirstIsland = True
                    break
            if foundFirstIsland:
                break
        
        return bfs()
        

"""
@functools.lru_cache(maxsize = None)
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
                
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        n = len(grid)
        m = len(grid[0])

        def calcDistance(pairA, pairB):
            # manhattan distance
            return abs(pairA[0] - pairB[0]) + abs(pairA[1] - pairB[1]) - 1

        def isOutOfBounds(x, y):
            return (x < 0 or x >= n or y < 0 or y >= m)

        def dfs(island, x, y):
            # fill the island point stores
            island.add((x, y))
            for dx, dy in directions:
                # out of bounds check
                # continue dfs
                newX = x + dx
                newY = y + dy
                if not isOutOfBounds(newX, newY) and grid[newX][newY] == 1 and (newX, newY) not in island:
                    dfs(island, newX, newY)

        
        islandA = set()
        islandB = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                if len(islandA) == 0:
                    dfs(islandA, i, j)
                elif len(islandB) == 0 and (i, j) not in islandA:
                    dfs(islandB, i, j)

        minDist = float("inf")
        for pairA in islandA:
            for pairB in islandB:
                minDist = min(minDist, calcDistance(pairA, pairB))
        
        return minDist
"""

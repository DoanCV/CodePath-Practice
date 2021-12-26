"""
A frog is crossing a river
    the river is divided up into units where each unit may or may not have a stone
    given a list of stone positions in ascending order, determine if the frog can cross the river
    
    aftwerwards, if the frog's last jump was k units the next jump is k-1, k or k+1 units
        the first two elements of the given array must be 0 then 1 since the frog assumes that position 0 to position 1 is the first k
        
We can use DFS but all the way at the bottom we see that in Python we get TLE.
Lets add memoization to optimize
"""
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        
        self.memo = set()
        
        return self.dfs_cross(stones, 1, 1, stones[len(stones) - 1])
    
    def dfs_cross(self, stones, unit, prestep, destination):
        
        if (unit, prestep) in self.memo:
            return False
        
        if unit == destination:
            return True
        
        if prestep <= 0 or unit not in stones: # unit > destination or unit < 0 not necessary
            return False
        
        for direction in (prestep - 1, prestep, prestep + 1):
            if self.dfs_cross(stones, unit + direction, direction, destination):
                return True
        
        self.memo.add((unit, prestep))
        return False

    
    
"""        
This looks like DFS on the possible moves
    try movement in all possible directions
    issue is I get TLE, same logic in java is fine though
    
Potential improvment - memoize states with a set    
"""

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        
        units = set()
        for i in range(len(stones)):
            if i > 0 and stones[i] - stones[i-1] > i:
                return False
            units.add(stones[i])
        
        return self.dfs_cross(units, 1, 1, stones[len(stones) - 1])
        
    def dfs_cross(self, units, unit, prestep, destination):
        if (prestep <= 0):
            return False
        
        if unit not in units:
            return False
        
        if unit == destination:
            return True
        
        if destination <= unit + prestep + 1 and destination >= unit + prestep - 1:
            return True
        
        return self.dfs_cross(units, unit + prestep + 1, prestep + 1, destination) or self.dfs_cross(units, unit + prestep, prestep, destination) or self.dfs_cross(units, unit + prestep - 1, prestep - 1, destination)

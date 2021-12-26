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

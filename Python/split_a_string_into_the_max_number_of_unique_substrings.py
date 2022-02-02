"""
DFS backtracking
we try every split and continue only if the previous substring splits do not already exist in a visited set
"""

class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        def backtrack(position, visited):
            
            substring_count = 0 
            
            if position < len(s):
                
                for i in range(position + 1, len(s) + 1):
                    if s[position:i] not in visited:
                        visited.add(s[position:i])
                        substring_count = max(substring_count, 1 + backtrack(i, visited))
                        visited.remove(s[position:i])
                        
            return substring_count
        
        return backtrack(0, set())

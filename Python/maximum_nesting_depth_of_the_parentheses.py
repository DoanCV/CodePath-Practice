"""
we count how many open parentheses there are
    substract when we see close
    ignore all other characters

get the maximum amount of open parentheses at any point since that is the max depth

"""

class Solution:
    def maxDepth(self, s: str) -> int:
        
        max_count = 0
        curr = 0
        
        for i in range(len(s)):
            
            if s[i] == "(":
                curr += 1
                
                if curr > max_count:
                    max_count = curr
                    
            elif s[i] == ")":
                curr -= 1
        
        return max_count
            

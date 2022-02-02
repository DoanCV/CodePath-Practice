"""
DFS backtracking

we will try slices of size 1 to 4 and see if it is <= 255
    if so we add that slice and a period to the path and continue
    
we will stop when we got to the last segment, which there should be 4
    also we will stop if we have a leading 0
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        result = []
        
        self.dfs(s, "", 0, result)
        
        return result
        
    def dfs(self, s, path, curr_series_count, result):
        
        if curr_series_count == 4:
            
            if not s:                               # we finished building the last segment
                result.append(path[:-1])            # leave out the last "."
                
            return                                  # backtrack
        
        for i in range(1, 4):
            
            if i <= len(s):
                
                if int(s[:i]) <= 255:
                    self.dfs(s[i:], path + s[:i] + ".", curr_series_count + 1, result)
                    
                # block out leading zero
                if s[0] == "0":
                    break

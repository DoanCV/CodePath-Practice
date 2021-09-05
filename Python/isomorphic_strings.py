"""
the given strings are the same length 

we will map the character of s to the character at t if the mapping does not exist
    if the match already exists and it is not the same then we return False
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # case 0: at most length 1 string, obviosuly the single characters map to each other and empty matches to empty
        if len(s) <= 1:
            return True
        
        hashmapStoT = {}
        hashmapTtoS = {}
        
        # loop through both strings
        for i in range(len(s)):
            
            # if not in map
                # if the value has not been mapped add it
            if s[i] not in hashmapStoT:
                if t[i] not in hashmapTtoS:
                    hashmapStoT[s[i]] = t[i]
                    hashmapTtoS[t[i]] = s[i]
                else:
                    return False
                
            # already in map
            else:
                # if different values return False
                if hashmapStoT[s[i]] != t[i]:
                    return False
        
        # return True
        return True

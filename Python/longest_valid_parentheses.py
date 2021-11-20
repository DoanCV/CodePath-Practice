"""
The idea is go through the string and use DP to store the longest valid parentheses at that point.
take example "()(())"
i : [0,1,2,3,4,5]
s : [(, ), (, (, ), )]
DP:[0,2,0,0,2,6]

We count all the "(" so far
If we find a ")" and "(" counter is not 0, we have at least a valid result size of 2, i.e. “()"
Check the the one before, i.e. (i - 1). If DP[i - 1] is not 0 means we have something like this “(())” . This will have DP = [0,0,2,4]
We might have something before "(())”. Take the "()(())” example, Check the i = 1 because this might be a consecutive valid string.

O(N) time complexity where N is the length of the given string. We solve in one pass. 
O(N) space complexity since we have an array of size N to keep track of the maximum length substring containign valid parentheses.
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        if len(s) <= 1:
            return 0
        
        longest = [0 for _ in range(len(s))]
        max_len = 0
        open_paren_count = 0
        
        for i in range(len(s)):
            if s[i] == "(":
                open_paren_count += 1
            
            # we have a ")" right now and the string so far can only be valid if open_paren_count is >= ")" count
            elif open_paren_count > 0:
                
                longest[i] = longest[i - 1] + 2 # we have a valid pair and a pair is length 2, add it to the previous index which could be holding nested pairs
                
                longest[i] += longest[i - longest[i]] if i - longest[i] >= 0 else 0 # add the previous adjacent valid sequence since we want contiguous length
                                
                max_len = max(longest[i], max_len)
                open_paren_count -= 1
        
        return max_len

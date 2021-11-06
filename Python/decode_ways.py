"""
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

We are given a string with a number (never empty)
    the digits map to letters from A-Z as shown above
    1-9 map but two digits like from 11-26 map also map to letters from A-Z
    this means there can be multiple ways to decode the string
        we can decode two digits or one digit at a time to get the same result
    
We have to find the number of ways the string can be decoded

This is very similar to climbing staircase since the steps are 1 at a time or 2 at a time
    knowing this we can store the number of ways to decode a given digit ie step in an array
    our base cases
        there is 1 way to decode get zero digits
        there is 1 way to get the first digit if not a leading zero
            we may have leading zeros
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        
        dp[0] = 1
        if s[0] != "0":
            dp[1] = 1
        else:
            dp[1] = 0
        
        for i in range(2, len(s) + 1):
            
            # one step
            if int(s[i-1:i]) > 0 and int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]
            
            # two steps
            if int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
            
        return dp[-1]

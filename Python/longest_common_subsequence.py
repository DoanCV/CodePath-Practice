"""
                            lcs("AXYT", "AYZX")
                           /                   \
             lcs("AXY", "AYZX")                 lcs("AXYT", "AYZ")
                /          \                      /            \ 
    lcs("AX", "AYZX") lcs("AXY", "AYZ")   lcs("AXY", "AYZ") lcs("AXYT", "AY")
    
when we fill in a cell dp[i,j], we need to already know the values it depends on, namely in this case dp[i+1,j], dp[i,j+1], and dp[i+1,j+1]
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
        return dp[m][n]

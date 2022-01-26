class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        count = 0
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                
                # if the ends of the substring are the same
                if s[i] == s[j]:
                    
                    # if the substring is at most length 3 then obviously the substring is palindrome
                    dp[i][j] = True if i + 1 > j - 1 else dp[i + 1][j - 1] 
                
                # if the substring is palindrome increase the count
                if dp[i][j]:
                    count += 1
        
        return count

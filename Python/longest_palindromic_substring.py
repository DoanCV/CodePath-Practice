"""
brute force:
    generate all substrings and check if each is a palindrome then keep track of the longest valid subtring
    this takes O(N^3) time since it takes N^2 to generate the substrings and then N time to check if each substring is a palindrome
    
    
dp:
bottom-up
    2-D grid
    
    rows are start index and columns are end index
        the main diagonal is going to be all True
    we will calcualte on slices of the string above the diagonal since our end > start otherwise we are going backwards
    
    when we check a slice we are checking if the boundary (start, end) are the same because compared to the rest of the string, we have already determined if it is a palindrome
    otherwise we are repeating calculations
    this is our subproblem

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # generate the grid
        dp = [[0] * len(s) for _ in range(len(s))]
        
        # fill diagonal with True
        for i in range(len(s)):
            dp[i][i] = True
        
        # single char is palindrome so this will be the shortest
        longest_substring = s[i]
        
        # fill above the main diagonal
            # start from the bottom and move up
                # stay to the right of the diagonal
        for start in range(len(s) - 1, -1, -1):
            for end in range(start + 1, len(s)):
                
                # if the boundary are the same
                if s[start] == s[end]:
                    
                    # if the slice is one char or if the inner substring is also palindrome
                    if end - start == 1 or dp[start + 1][end - 1] == True:
                        
                        # set current position to True
                        dp[start][end] = True
                        
                        # check if the current susbtring is the longest
                        if len(longest_substring) < len(s[start : end + 1]):
                            longest_substring = s[start : end + 1]
                        
        # return answer
        return longest_substring 

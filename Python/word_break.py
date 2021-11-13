"""
All the words are unqiue and they are all lowercase

DP with a 1-D array of bools

keep track of the position in the given string 
    the index is true if there is a word in worddict that ends at that index in the given string
        we also need to check that word starts its length before

"leetcode", wordidct = ["leet", "code"]
      l  e  e  t  c  o  d  e
dp = [F, F, F, F, F, F, F, F]
     nc nc nc  T nc nc nc  T

this works since at dp[-1]

O(s^3) time complexity since splicing takes linear time and we have nested for loop over our string s. In the worst case we splice the entire string. 
O(s + len(wordDict)) space complexity since the space we use is the boolean array and the set. The size of the set is the number of words in our wordDict and our boolean array is of size s + 1.
"""
# cleaner solution
# use a set to have constant lookup to see if a word exists in wordDict
# use two pointers, one at the start of the substring and one at the end
    # we use this to splice
# our dp array and loop bounds should be 1 larger than the length of the given string to avoid going out of bounds for the first word check
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set(wordDict)
        
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
    
        for i in range(len(s) + 1):
            for j in range(i + 1, len(s) + 1):
                
                if s[i:j] in wordSet and dp[i] == True:
                    dp[j] = True
                    
        return dp[-1]
    
"""
# O(k * s^2) time complexity
# O(s) space complexity
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False for _ in range(len(s))]
        
        for i in range(len(s)):
            for word in wordDict:
                
                # check if the full word is there and if the previous word has been checked
                    # there may not be a preivous word since the current word is the first word
                if word == s[i - len(word) + 1: i + 1] and (dp[i - len(word)] or i - len(word) == -1):
                    dp[i] = True
        
        return dp[-1]
"""

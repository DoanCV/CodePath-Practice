"""
Given an array of strings, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.
    an uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others



we can check each string if it is a subsequence of any other string
    if a string is not a subsequence of any other string i.e. it is uncommon, we will try to update the max length
    if no string found, we will return -1
    
    
O(k * N ^ 2) time complexity where N is the number of strings in the given list and k is the average length of each word. We try eveyr pair of strings which is N^2 in time but we have to check if the strings are subsequences of each other so that time grows with the length of the word. 
O(1) space complexity since we solve in place
"""

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        
        def isSubsequence(str1, str2):
            # start at the beginning and if all the characters in one string exists in the smae relative order in the other then one is subsequence of the other
            a = len(str1)
            b = len(str2)
            
            while a > 0 and b > 0:
                i = len(str1) - a
                j = len(str2) - b
                
                if str1[i] == str2[j]:
                    a -= 1
                b -= 1
            
            return a == 0 # if there are still letters left over for one of the strings, we know they are not subesequences of each other

            
        max_len = -1
        for i in range(len(strs)):
            
            isNotUncommon = 0
            curr_len = len(strs[i]) # the longer string is the longest uncommon subsequence but since we check every pair we can write it like this
            
            for j in range(len(strs)):
                
                if i != j and isSubsequence(strs[i], strs[j]) == 1:
                    isNotUncommon = 1
                    break
            
            if not isNotUncommon:
                max_len = max(max_len, curr_len)
                    
        return max_len

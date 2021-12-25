"""
return the length of the longest uncommon subsequence between strings a and b. If the longest uncommon subsequence does not exist, return -1.

an uncommon subsequence between two strings is a string that is a subsequence of one but not the other


if the two strings are the same then there is no answer
otherwise 
    if they have different lengths the longer string is the answer
    if they have the same length already know they are not equal so the length of either string is the answer

"""

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))

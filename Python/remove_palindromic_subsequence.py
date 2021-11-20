"""
we have a string of just a and b
    we can remove palindromic subsequences, one at a time
    find the minimum number of steps to make the string empty

observation, subsequence so we can get rid of all the a and all of the b
    this is 2 steps so this is worst case answer

if the entire string is already a palindrome then our answer is 1
    we will not have empty string so literally the answer is either going to be 1 or 2

check if the string is a palindrome, if so the answer is 1 else if we have both a and b in the string then the answer is 2

"""

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        if s == s[::-1]:
            return 1
        else:
            return 2

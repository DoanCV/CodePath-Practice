"""
Find if the given number is a palindrome
    All numbers are valid integers
    Note negative numbers are not integers since the negative sign does not ever come at the end


We cant iterate on integer unless wo do bit manip so just turn to string and use two pointers just like a normal palindrome check
OR
We can build the number flipped to compare if the values are the same
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        copy = x
        result = 0
        
        while copy > 0:
            
            result = result * 10 + copy % 10
            copy = int(copy // 10)
        
        return result == x

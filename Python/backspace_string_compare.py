"""
U
Given two strings, return True if they are equal when both are typed into text editors where a "#" is a backspace
    backspace on character deletes it and after backspacing an empty text, the text will continue empty

M/P
Traverse backwards and compare character by character, make sure to skip "#"

if we see backspace skip and keep track of the number of # we see
    if we still have leftover # we need to keep skipping
    if we see see # we will need to increment to know to skip that many characters

if the characters dont match then return False
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        i = len(s) - 1
        j = len(t) - 1
        
        s_backspaces = 0
        t_backspaces = 0
        
        while True:
            
            while i >= 0 and (s_backspaces or s[i] == "#"):
                if s[i] == "#":
                    s_backspaces += 1
                else:
                    s_backspaces -= 1
                
                i -= 1
                
            while j >= 0 and (t_backspaces or t[j] == "#"):
                if t[j] == "#":
                    t_backspaces += 1
                else:
                    t_backspaces -= 1
                
                j -= 1
            
            # one is out of index so they are not the same
            # the characters are not the same
            # these two conditions can be condensed to the following
                # if not (not done comparing and the characters are the same)
                # if done comparing or the characters are not the same
                    # return True if both are done comparing otherwise the strings are not the same
            if not (i >= 0 and j >= 0 and s[i] == t[j]):
                return i == j == -1
            
            i -= 1
            j -= 1

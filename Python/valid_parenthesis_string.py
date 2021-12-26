"""
U
Given a string s that contains "(", ")", "*" where "*" can be treated as "(", ")" or an empty string
    return true if s is valid

ex. "("
this string by itself is not valid
    however what can make it valid
    one ")" right after will make it work
    in this case we are expecting a minimum of 1 ")" and a maximum of 1 ")"
    
ex. "(*("
this string by itself is not valid
    however what can make it valid
    one or two or three ")" right after will make it work
    in this case we are expecting a minimum of 1 ")" and a maximum of 3 ")"

M
in other valid parentheses problems we can get the count of "(" to determine the number of ")" that we need if there are more ")" than "(" we immediately return false
    we can do something similar

P
Have one counter (cmax) for counting the maximum number of ")" we can accommodate with current left braces and stars
    if cmax becomes negative, it means we can’t accommodate current right braces with current left braces and stars. So, we return false.
Have a second counter (cmin) which represents the minimum number of ")" that must be there further to make sure the whole string is valid 
    this number can’t be negative, so if it becomes negative then we put it to zero
In the end if cmin is positive then it means that we need more ")" to make sure the overall string is valid. So, we check whether cmin is zero or not and return the answer


when we see a "(" increment the max and min
when we see a ")" decrement the max and min
when we see a "*" increment the max and decrement the min

IR

E
O(N) time complexity where N is the length of the given string. We solve in one pass.
O(1) space complexity

"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        cmax = 0
        cmin = 0
        
        for i in range(len(s)):
            
            if s[i] == "(":
                cmin += 1
                cmax += 1
            elif s[i] == ")":
                cmin -= 1
                cmax -= 1
            elif s[i] == "*":
                cmin -= 1
                cmax += 1
            
            if cmax < 0:
                return False
            
            cmin = max(cmin, 0)
        
        return cmin == 0

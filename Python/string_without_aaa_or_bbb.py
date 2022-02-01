"""
greedy approach

s = a + b

while a + b < s
    start with the greater of the two
    
    if prev 2 arent the same
        add greater update frequency 
    else
        add the other and update frequency
    
"""

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        result = []
        
        while a + b > 0:
            
            s = len(result)
            
            if s > 1 and result[-2] == result[-1]:
            
                if result[-1] == "a":
                    result.append("b")
                    b -= 1
                else:
                    result.append("a")
                    a -= 1
            
            else:
                
                if a > b:
                    result.append("a")
                    a -= 1
                else:
                    result.append("b")
                    b -= 1

        return "".join(result)

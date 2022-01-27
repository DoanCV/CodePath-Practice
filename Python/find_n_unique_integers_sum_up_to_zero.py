"""
we need to find n unique integers that add up to 0
    return any valid answer
    answer has to be sorted? sure why not
    
if we find an integer, also add its complement
    this gives us n integers if even
    if odd, 0 is integer so we just add that kekW

"""

class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        answer = []
        
        for i in range(1, n // 2 + 1):
            answer.append(i)
            answer.append(-i)
        
        if n % 2 == 1:
            answer.append(0)
        
        return answer
    
"""
class Solution:
    def sumZero(self, n: int) -> List[int]:
        return range(1 - n, n, 2)

"""

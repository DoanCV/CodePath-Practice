"""
Two thoughts:
1. Brute force
we can multiply x by itself n times
    if n is negative we 1/x first then multiply it by itself n times
    this is linear in time

2. logN
we can split up N // 2
    ex. 2^10
    x = 2, N = 10
    
    x^N
    = x^5 * x^5
    when we have odd exponent we can have even and then multiply by x
    = x^2 * x^2 * x * x^5 
    
    if we have negative then 1/x and feed in -N

we can implement this recursively or iteratively
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # handle 0 exp
        if n == 0:
            return 1
        
        # handle negative exp
        if n < 0:
            return self.myPow(1/x, -n)
        
        # keep splitting 
        factor = self.myPow(x, n//2)
        
        # handle positive exp: odd, even
        if n % 2 == 0:
            return factor * factor
        if n % 2 == 1:
            return factor * factor * x

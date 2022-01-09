"""
instead of dp which i did in cpp:

mathematical observation
We have to take m-1 steps down and n-1 steps to the right since we want to go from the top left corner to the bottom right corner
    At each step we can either choose to go right or down
    
Therefore, the number of possible paths is equal to:
(m + n - 2) C (n-1)
    where m - 1 + n - 1 = m + n - 2

x C y = x! / ((x-y)! * y!)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m + n - 2) // factorial(m-1) // factorial(n-1)

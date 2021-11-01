"""
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9] len = 9
we are starting from the left
we remove the odds

arr = [2, 4, 6, 8] len = 4
we are starting from the right
we remove the evens

arr = [2, 6] len = 2
we are starting from the left
we remove the odds

arr = [6] len = 1
we are done bc of length 1


another ex for logic purposes
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] len = 10
    skip = 1 -> 2
arr = [2, 4, 6, 8, 10] len = 5
    we are starting from the right but the head element changes
    skip = 2 -> 4


the thing is we notice that every time we eliminate we only care about the a few of the numbers not all
    obviously when we are at length 1 we are done this means we need to keep track of length and what is the first value
    we can split into cases to see what the first value should be
        that way we do not need to create an array of values from 1 to n to simulate the game
    we can have a flag to know if we are going right or left
    we can also have a variable to denote how many values are left which tells us when to stop and how to identify our cases

cases:
    we are going left
        odd length arr
            the head value changes so we will need to skip
            the amount we skip double each time since we just removed elements
        even length arr
            skip anyways
            seems like length dont matter for left
    
    we are going right
        odd length arr
            the head value will change skip as usual
            
        even length arr
            the head value will not change
    
"""

class Solution:
    def lastRemaining(self, n: int) -> int:
        num_elements_remaining = n
        skip = 1
        head = 1
        
        start_left = True
        
        while num_elements_remaining > 1:
            
            if start_left or num_elements_remaining % 2 == 1:
                head = head + skip
                
            num_elements_remaining = num_elements_remaining // 2
            skip *= 2
            start_left = not start_left
            # start_left = 1 - start_left
            # is also equivalent 
            
        return head

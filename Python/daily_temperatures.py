"""
U
we have an array of positive integers (30 <= temperatures[i] <= 100) representing temperatures
    we want to know the number of days from the current temperature until we we a warmer day

return an array, answers, where answers[i] is the number of days to wait after the ith day to get a warmer temperature
    if there is no answer then answer[i] == 0

seems like the last index is always == 0 since there is no temperatures after

warmer means higher value in temperature array


M
similar to next greatest linkedlist node, this time we dont have linkedlist
    we use a stack

we will store the value and the index in the stack


P
if the day with higher temperature is not found, we leave the answer to be the default 0

check whether the current temperature is greater than the last appended stack value
    pop all the elements which is less than the current temperature
    the number of days is the current index - the one we popped

ex.
[30,60,90]

    index = 0
    stack is empty
    [(0, 30)]
    result = [0, 0, 0]

    index = 1
    30 < 60
        popped_index = 0
        1 - 0 = 1
        result = [1, 0, 0]
    [(1, 60)]

    index = 2
    60 < 90
        popped_index = 1
        1 - 0 = 1
        result = [1, 1, 0]
    [(2, 90)]

    result = [1, 1, 0]  
    
IRE

"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]
        
        for index, value in enumerate(temperatures):
            
            while stack and stack[-1][1] < value:
                
                popped_index, _ = stack.pop()
                
                result[popped_index] = index - popped_index
                
            stack.append([index, value])
        
        return result

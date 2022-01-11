"""
U
we are given an array and a window size
    the window is moving from left to right

we can only see the elements in the window, return the max values in the window for every time it moves

M
deque

P
we can use a deque to keep track of the candidates for the maximum
    each time we slide the window, only two elements change
    there is no reason for us to continuously scan the entire window for the maximum

pop the end indexes of smaller elements (they'll be useless)
append the current index
pop the front if it's still in the deque (it falls out of the window)
if our window has reached size k, append the current window maximum to the output

"""
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        d_queue = deque()
        
        for index, value in enumerate(nums):
            
            # make sure leftmost element is the largest
            while d_queue and nums[d_queue[-1]] <= value:
                d_queue.pop()
            
            d_queue.append(index)
            
            # maintain size k
            if index - d_queue[0] >= k:
                d_queue.popleft()
              
            # if we are at window size the append the maximum to the output
            if index >= k - 1:
                output.append(nums[d_queue[0]])
        
        return output

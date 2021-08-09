####### DUPLICATE OF SQUARE ARRAY ##################

import math # for absolute value

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        brute force:
        square, append to new array, then sort
        not good since you have to sort something that was already sorted
        
        
        two pointer:
        either start at the ends or find where the sign changes if at all
        
        do not let the pointers cross, if they do we are done
        if the end is greater in magnitude we add the square of it in the array and move the pointer
            same idea with the pointer at the start
        then append to the array in reverse order
        """
        
        start = 0
        end = len(nums) - 1
        output = []
        
        # they can overlap in the 0 case which has the lowest magnitude
        while start <= end:
            if abs(nums[start]) > abs(nums[end]):
                output.insert(0, nums[start] ** 2)
                start += 1
            else:
                output.insert(0, nums[end] ** 2)
                end -= 1
        
        return output
      
# O(N) time complexity, where N is the length of the given array, since we traverse once through the array but in N/2 steps.
# O(1) space complexity if we ignore the output array since we are not using any extra data structures. Otherwise O(N) since our output is supposed to be the same length as our input array.

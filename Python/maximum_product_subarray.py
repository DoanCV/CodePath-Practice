"""
Given an integer array, find the contiguous subarray with the largest product and return that product
    there can be 0s in the given array

we know that even number of negatives is fine since that makes the answer positive with the product of the entire array as the greatest magnitude
    however, odd number of negatives forces us to take a closer look
        we could just remove a negative but which one?
            the first one or the last one only since if we get rid of one in between then we lost the greatest possible magnitude


One pass approach, dynamic programming
    keep track of three things
        the current value - the individual value could be the greatest, unlikely but possible, consider array with 0s and one positive integer 
        the minimum product - if we have the minimum then the next sign flip can make that the maximum
        the maximum product - obvious enough

"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = 1
        curr_max = 1
        max_product = float("-inf")
        
        for num in nums:
            values = [num, num * curr_min, num * curr_max]
            
            curr_min = min(values)
            curr_max = max(values)
            
            max_product = max(max_product, curr_max)
        
        return max_product
    
"""
Two passes approach
    first pass includes everything
    second pass starts from the end and compares the current product with the result of the first
        that way a negative is dropped at some point when we call max()
    if we get a prodcut of 0 reset it to 1 since otherwise that would make every other step 0 and we miss out on the correct answer
    
"""
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = float("-inf")
        
        curr_product = 1
        for num in nums:
            curr_product *= num
            max_product = max(curr_product, max_product)
            if curr_product == 0:
                curr_product = 1
            
        curr_product = 1
        for i in range(len(nums) - 1, -1, -1):
            curr_product *= nums[i]
            max_product = max(curr_product, max_product)
            if curr_product == 0:
                curr_product = 1
        
        return max_product
        
"""

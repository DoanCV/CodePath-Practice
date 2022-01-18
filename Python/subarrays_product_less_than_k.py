"""
Given k, return the number of subarrays whose product is less than k

Sliding window

"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        window_start = 0
        window_end = 0
        curr_product = 1
        count = 0
        
        while window_end < len(nums):
            curr_product *= nums[window_end]
            
            while window_end >= window_start and curr_product >= k:
                curr_product /= nums[window_start]
                window_start += 1
            
            count += window_end - window_start + 1
            
            window_end += 1
            
        return count

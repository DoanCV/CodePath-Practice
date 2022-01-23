"""
Sliding window
    expand window until the window sum is equal to the target
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("inf")
        
        window_start = 0
        curr_sum = 0
        for window_end in range(len(nums)):
            
            curr_sum += nums[window_end]
            
            while curr_sum >= target:
                min_length = min(min_length, window_end - window_start + 1)
                curr_sum -= nums[window_start]
                window_start += 1
            
        
        if min_length == float("inf"):
            return 0
        else:
            return min_length

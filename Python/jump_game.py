"""
Update the max index that I can reach
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        curr_max = 0
        for i in range(len(nums)):
            
            curr_max = max(curr_max, i + nums[i])
            
            if curr_max >= len(nums) - 1: # can reach the end
                return True
            
            if curr_max <= i: # cant reach current index
                return False
            
        return False

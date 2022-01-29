class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        # we can return early if we see 0
        # also we just care about the sign so if we see a negative we flip
        
        answer = 1
        for num in nums:
            
            if num == 0:
                return 0
            
            if num < 0:
                answer *= -1
        
        return answer

"""
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        result = 1
        for i in range(len(nums)):
            result *= nums[i]
            
        if result == 0:
            return 0
        elif result > 0:
            return 1
        else:
            return -1
            
"""

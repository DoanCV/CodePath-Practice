"""
have a set to store the subset sums we encounter
    however, we cant update the set while iterating over it so we make a copy

"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # the sum of the elements has to be divisible by 2 otherwise we cant split
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        
        dp = set()
        dp.add(0) # we can choose to ignore a value
        
        for i in range(len(nums) - 1, -1, -1):
            
            temp = set(dp) # make a copy
            for partition in dp:
                temp.add(partition + nums[i])
                
            dp = temp
        
        return True if target in dp else False

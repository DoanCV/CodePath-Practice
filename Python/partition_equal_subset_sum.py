"""
U
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

The subset sum has to be half the sum of all the elements of the given array so if that sum is not divisible return False


M/P
have a set to store the subset sums we encounter
    however, we cant update the set while iterating over it so we make a copy
    
base case:
    we can ignore a value so the sum of nothing is 0

for each element 
    go through each element of the set
        add the sum to the set
we have created all the subsets and now we need to see if the target exists

E
O(N * sum(nums)) time complexity where N is the length of the given array, nums. The size of our set is limited to the sum of the elements in the given array.
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # the sum of the elements has to be divisible by 2 otherwise we cant split
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        
        dp = set()
        dp.add(0) # we can choose to ignore a value
        
        for i in range(len(nums)):
            
            temp = set(dp) # make a copy
            for partition in dp:
                temp.add(partition + nums[i])
                
            dp = temp # update the set
        
        return True if target in dp else False

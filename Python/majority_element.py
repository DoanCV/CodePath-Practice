"""
U
given an array of size n, return the majority element
    the majority element is the element that appears more than floor(n/2) times
    we are always guranteed a majority element

M/P
idea 1:
going off of the assumption we can sort and return the middle element since that will always include the majority element

idea 2:
we can also scan linearly and store the frequency as we go
    once we hit n // 2 + 1 we found the majority element

idea 3:
or we can use the boyer moor's algorithm
    here we assume the first element is the majority element and keep track of a count
    if the element is the same we increment the count
    if the element is not the same then we decrement the count
        if the count is now 0 then we make the current element the candidate for the majority element
        
    as long as in the end the count is positive we know out current candidate is the majority element

    what we are doing by decrementing the count is taking away the other elements
        we know that the majority element will have a greater frequency then the rest of the entire array
        when we find the correct candidate it will stay positive
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        
        result = nums[0]
        
        for i in range(1, len(nums)):
            
            if nums[i] != result:
                count -= 1
                
                if count == 0:
                    result = nums[i]
                    count = 1
            
            else:
                count += 1
                
        return result
        
        
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)
        
        for i in range(len(nums)):
            
            freq_map[nums[i]] += 1
            
            if freq_map[nums[i]] > len(nums) // 2:
                return nums[i]
"""        
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
    
"""

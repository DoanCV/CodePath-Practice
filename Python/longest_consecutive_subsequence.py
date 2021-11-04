"""
:komodoGIGA: I do not need top down dp

I can add all elements to a set

we then loop through each element of the given array
    treat every number as a start
    if the element - 1 is in the set then we ignore it since we already found the (element - 1)th element and accounted for its sequence
    
    else we found a start
        find the end since sequences are consecutive
        keep track of the length of the sequence
    
    update the max sequence length

return the max sequence length

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums_set = set(nums)
        
        for num in nums:
            
            if num - 1 in nums_set:
                continue
            else:
                sequence_num = num
                while sequence_num + 1 in nums_set:
                    sequence_num += 1
                
                max_len = max(max_len, (sequence_num - num + 1) )
                
        return max_len

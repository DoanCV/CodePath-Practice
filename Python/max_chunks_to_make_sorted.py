"""
If the maximum from the left (inclusive) is less than or equal to the 
        minimum from the right, we create a chunk there because there is no value 
        to the right of the current subarray that would be required to be sorted 
        with the left chunk
"""

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 1
        
        min_values_from_right = []
        curr_min = float("inf")
        for i in range(len(arr) - 1, -1, -1):
            curr_min = min(arr[i], curr_min)
            min_values_from_right.append(curr_min)
        min_values_from_right = min_values_from_right[::-1]
        
        max_values_from_left = []
        curr_max = 0
        for i in range(len(arr) - 1):
            curr_max = max(curr_max, arr[i])
            if curr_max <= min_values_from_right[i + 1]:
                chunks += 1
                
        return chunks
        
        

"""
FROM LC DISCUSS: A STACK BASED SOLUTION

when we encounter an element, the very first thing we think must be: how can we use this element and will this element still be needed?

To the first question, this element is used to determine if it must be together with the previous greater elements.

To the second question, once this element is removed, it will no longer be needed. Reason is:

Considering the array with order of 4,5,4,3, When 4 came in the stack (now 4,5), 5 was removed because 5,4 must be a chunk. Then 3 came in, does it need to know the existence of 5 and 4(the second 4)? As long as 4(the first 4) and 3 must be in the same chunk , all the elements between 4(the first 4) and 3 should be in the same chunk.

no element will be visited over twice, this is a O(N) time


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        
        for num in arr:
            local_max = num
            
            while len(stack) > 0 and stack[-1] > num:
                local_max = max(local_max, stack.pop())
            
            stack.append(local_max)
        
        return len(stack)
"""    

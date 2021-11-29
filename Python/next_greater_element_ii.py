"""
put all indexes into the stack, smaller index on the top
then we start from end of the array look for the first element (index) in the stack which is greater than the current one
that one is guaranteed to be the next greater element
then put the current element (index) into the stack

"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        results = [-1 for _ in range(len(nums))]
        
        for i in range(len(nums) - 1, -1, -1):
            stack.append(i)
        
        for i in range(len(nums) - 1, -1, -1):
            
            while len(stack) > 0 and nums[i] >= nums[stack[-1]]:
                stack.pop()
                
            if len(stack) > 0:
                results[i] = nums[stack[-1]]
            
            stack.append(i)

        return results
            

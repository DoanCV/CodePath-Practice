"""
Get the sum of all the elements

then keep track of a sum of what we see so far in a loop
    subtract what we see
    
    if they match then return the current index
    
    add the current value if we are not done
    
ex.
[1,7,3,6,5,6]
left = 0
right = 28

i = 0
right = 27
left = 1

i = 1
right = 20
left = 8

i = 2
right = 17
left = 11

i = 2
right = 11
right is equal to left so return i - 3 since the sum of elements to the left of i = 3 is 11 and so is the right sum


ex.
[2,1,-1]
initalize:
left = 0
right = 2

i = 0
right = 0
left and right are equal return i = 0 since the sum of elements to the left of i = 0 is 0, because there are no elements, and so is the right sum


"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        
        for i in range(len(nums)):
            right -= nums[i]
            
            if right == left:
                return i
            
            left += nums[i]
            
        return -1

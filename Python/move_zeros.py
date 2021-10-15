"""
Loop through the array
    keep a pointer on the last 0 encountered
    
    we will encounter either a 0 or nonzero

i = 0
[0,1,0,3,12]
 ^
i = 1
[1,0,0,3,12]
   ^
i = 2
[1,0,0,3,12]
   ^
i = 3
[1,3,0,3,12]
     ^
i = 4
[1,3,12,3,12]
        ^

we are now at the end
fill the rest after the pointer with 0s

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ptr = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[ptr] = nums[i]
                ptr += 1
            
        for curr_pos in range(ptr, len(nums)):
            nums[curr_pos] = 0

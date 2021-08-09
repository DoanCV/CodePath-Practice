"""
Math:
just add them all up we know summation from 1 to n, it's just n * (n + 1) / 2. then we subtract the summation from the sum of our array which gives us the answer. 

cyclic sort:
while we are not at the end
  check if the current value is equal to the current index
    we will have to swap if they are not the same
  
"""

def find_missing_number(nums):
  curr_sum = 0
  for i in range(len(nums)):
    curr_sum += nums[i]

  return len(nums) * (len(nums) + 1) / 2 - curr_sum 

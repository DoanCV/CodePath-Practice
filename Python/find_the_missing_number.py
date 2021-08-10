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


def find_missing_number(nums):

  i = 0
  while i < len(nums):
    correct = nums[i]
    # we cant include N since we have an array of size N but N + 1 possible numbers
    if correct < len(nums) and nums[i] != nums[correct]:
      nums[i], nums[correct] = nums[correct], nums[i]
    else:
      i += 1
  
  for i in range(len(nums)):
    if i != nums[i]:
      return i
    
# O(N) time complexity, where N is the length of the given array, since in the worst case we will swap n - 1 times before incrementing i and then we find that out missing number is at the end.
# O(1) space complexity since we are not using any extra data structures.

"""
# we only have one number being duplicated but it can be duplicated multiple times
# we are guranteed a duplicate 

Cyclic sort:
while we are not at the end of the array

  if the current value is in the wrong position

    if the value at the position of the current value is not the same 
      we swap
    otherwise the two values we are swapping are the same then we found our duplicate

  else
    increment the current position

"""

def find_duplicate(nums):
  i = 0
  while i < len(nums):
    
    if nums[i] - 1 != i:

      current = nums[i] - 1
      if nums[i] != nums[current]:
        nums[i], nums[current] = nums[current], nums[i]  # swap
      else:  # we have found the duplicate
        return nums[i]

    else:
      i += 1

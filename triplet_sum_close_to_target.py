""" 
two pointer after sorting

keep track of:
left
right
min_diff = really large or inf
  we want to minimize this
target_sum - min_diff
  return value

logic:

sort the given array
initialize min_diff

loop through (the length of the array - 2) since we are looking at triplets, i gets up to lest two theres no point in checking

  # intialize left and right of the remainder of the array to see if a pair (left,right) and current value are close
  left = i + 1
  right = len(arr) - 1

  while left < right:
    curr_diff = target_sum - arr[i] - arr[left] - arr[right]
    
    # perfect match, return sum of the triplet
    if curr_diff == 0:
      return arr[i] + arr[left] + arr[right]
    
    # save new min if possible
      # curr magnitude < min magnitude then we're good
      # but differences can be +/- so we need to check when comment above isnt true
        # take the positive one when the magnitudes are equal (have multiple answers)
    if abs(curr_diff) < abs(min_diff) or (abs(curr_diff) == abs(min_diff) and curr_diff > min_diff)
      min_diff = curr_diff

    # move pointers closer
    if curr_diff > 0:
      left += 1
    else:
      right -= 1
return target_sum - min_diff
"""

import math
def triplet_sum_close_to_target(arr, target_sum):

  min_diff = math.inf
  arr.sort()
  
  for i in range(len(arr) - 2):
    left = i + 1
    right = len(arr) - 1

    while left < right:
      curr_diff = target_sum - arr[i] - arr[left] - arr[right]
      
      if curr_diff == 0:
        return arr[i] + arr[left] + arr[right]

      if abs(curr_diff) < abs(min_diff) or (abs(curr_diff) == abs(min_diff) and curr_diff > min_diff):
        min_diff = curr_diff
      
      if curr_diff > 0:
        left += 1
      else:
        right -= 1
  return target_sum - min_diff

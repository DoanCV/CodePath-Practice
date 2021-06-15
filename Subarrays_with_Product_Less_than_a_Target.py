"""
sliding window since contiguous subarray, we are not sorting since we lose the order of subarrays

keep track of:
results
  return value
  array of arrays, we will append valid answers
window_start = 0
window_end
curr_product = 1
  we only have positive numbers but this is the multiplication version of += and -= which we will divide out if product too high
curr_array
  we need to get rid of duplicates so we'll have to traverse the current window values backwards 
  we can loop since we know all subarrays from left to right of the window is less than target


logic:
intialize variables

loop through the length of the array with window_end
  update curr_product by multiplying it by the value at window_end

  # greater than or equal to
    # shrink the window
  while curr_product >= target:
    curr_product /= arr[window_start]
    window_start += 1

  # append since valid
    # use a deque (pronounced 'deck')
  
return results
"""
from collections import deque
def find_subarrays(arr, target):
  results = []
  window_start = 0
  curr_product = 1

  for window_end in range(len(arr)):
    curr_product *= arr[window_end]

    while curr_product >= target and window_start < len(arr):
      curr_product /= arr[window_start]
      window_start += 1

    curr_array = deque()
    for i in range(window_end, window_start - 1, -1):
      curr_array.appendleft(arr[i])
      results.append(list(curr_array))
  return results

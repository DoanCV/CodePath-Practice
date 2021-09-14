""""
two pointers since we can keep track of where the last 0s and the last 1s are

keep track of:
low = 0
  0s are to the left of this
high = len(arr) - 1 
  2s are to the right of this
curr = 0
arr
  return value
  given to us but we need to sort in place so no new data structures, auxillary is ok

logic:
initialize variables

# in between low and high inclusive are all the 1s
while current position is <= high:
  if value of current position is 0:
    # swap
    # increment low by 1 since the left of low must have all the 0s
    # increment current position by 1
    arr[current position], arr[low] = arr[low], arr[current position]
    low += 1
    current position += 1
  elif value of current position is 2:
    # swap
    # decrement high by 1 since the right of high must have all the 2s
    # do not increment curr by 1 since we have not checked what is at the new current position
    arr[current position], arr[high] = arr[high], arr[current position]
    high -= 1
  else:
    # we have a 1 since we check the other two possible values at any index of the given array
    current position += 1
return arr
"""

def dutch_flag_sort(arr):
  low = 0
  high = len(arr) - 1
  curr = 0
  while curr <= high:
    if arr[curr] == 0:
      arr[curr], arr[low] = arr[low], arr[curr]
      low += 1
      curr += 1
    elif arr[curr] == 2:
      arr[curr], arr[high] = arr[high], arr[curr]
      high -= 1
    else:
      curr += 1
  return arr

# O(N) time complexity, where N is the size of the given array, since we traverse the length of the array once. 
# O(1) space complexity since we are not using any new data structures.

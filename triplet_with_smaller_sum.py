"""
two pointer since i can sort the array and then for each element in the array i can check the rest of the array with the pointers

keep track of:
left
right
curr_sum
  we use this to compare with the target value
count
  return value
  return 0 if no triplet is less than target

logic:
initialize count = 0
sort the array

for loop over the length of the sorted array - 2 since when we get up to the last two elements, we no longer have a triplet
  # initialize left and right
  left = i + 1
  right = len(arr) - 1

  while left < right:
    curr_sum = arr[i] + arr[left] + arr[right]

    if curr_sum < target:
      # arr[right] > arr[left] so any thing less than arr[right] also work
      count += right - left
      left += 1
    else:
      right -= 1

return count
"""

def triplet_with_smaller_sum(arr, target):
  count = 0
  arr.sort()

  for i in range(len(arr)):
    left = i + 1
    right = len(arr) - 1

    while left < right:
      curr_sum = arr[i] + arr[left] + arr[right]

      if curr_sum < target:
        count += right - left
        left += 1
      else:
        right -= 1
  return count

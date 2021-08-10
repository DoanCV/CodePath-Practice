"""
# numbers range from 1 to n so we will have to shift

Find the missing number but with an array output
we will use cyclic sort

while we are not at the end of the given array
  if the current value is not the same as that of its index
    move it to the correct position by swapping

  else:
    increment the current position

loop through the "sorted" array
  if the values do not match, append to the output array

return the output array
"""

def find_missing_numbers(nums):
  i = 0
  while i < len(nums):
    current = nums[i] - 1
    if nums[i] != nums[current]:
      nums[i], nums[current] = nums[current], nums[i]
    else:
      i += 1

  missingNumbers = []
  for i in range(len(nums)):
    if i != nums[i] - 1:
      missingNumbers.append(i + 1)

  return missingNumbers

# O(N) time complexity, where N is the length of the given array, since in the worst case where we keep swapping the elements without incrementing we can only do taht N - 1 times and then traverse to the end without any additional steps. Then we loop once more linearly. N - 1 + N + N is still O(N).
# O(N) space complexity since in the worst case our output array has N - 1 numbers since every number is the same in the given array so N - 1 numbers are missing.

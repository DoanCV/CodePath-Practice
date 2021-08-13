"""
cyclic sort

while we are not at the end of the list
  if the current is not in the right position
    swap
  else
    increment position

loop through the list
  if there is a difference, append to the result since it is a duplicate but check if it is already in the results
"""

def find_all_duplicates(nums):
  
  i = 0
  while i < len(nums):
    correct = nums[i] - 1
    if nums[i] != nums[correct]:
      nums[i], nums[correct] = nums[correct], nums[i]
    else:
      i += 1
  
  duplicateNumbers = []

  for curr in range(len(nums)):
    if nums[curr] - 1 != curr:
      if curr not in duplicateNumbers:
        duplicateNumbers.append(nums[curr])

  return duplicateNumbers

# O(N) time complexity, where N is the length of the given list.
# O(1) space complexity if we ignore the output array.

"""
The size of our result is the same as that of the given array
  we know out elements are in the range 1 to n
lets line it up with our indicies

when we traverse through the array we know the current value
  interestingly this is also one more than the index where it should be (bc we are indexing from 0)
  since we know these two things we can swap the current value with whatever value is at the correct index since we know it doesnt belong there
  we will only move on if the current index is correct
"""

def cyclic_sort(nums):
  
  i = 0
  while i < len(nums):
    correct = nums[i] - 1
    if nums[i] != nums[correct]:
      nums[i], nums[correct] = nums[correct], nums[i]
    else:
      i += 1
  return nums

# O(N) time complexity, where N is the length of the given array, since in the worst case we have to swap n-1 elements without incrementing i but once we do that we continue to iterate to the end since no more chnages are necessary. This is n - 1 + n which is still linear.
# O(1) space complexity since the sort is done in place.

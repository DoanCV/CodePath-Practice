"""
https://www.youtube.com/watch?v=eLDT92Q0D9U&t=3s

First thought:
check adjacent elements
  loop through the difference between the elements since everything in between is missing
    add the missing numbers to min heap
pop heap k times and the last one we popped is our answer
slow

Second thought:
[4,7,9,10]

7 - 4 - 1 = 2 missing numbers
9 - 4 - 2 = 3 missing numbers
generalize to nums[i] - nums[0] - i 

use this to direct our binary search
  we find the first location where there are more than k missing numbers

"""
class Solution:
  def missingElement(self, nums, k):

    def missing_numbers(curr_index):
      return nums[curr_index] - nums[0] - curr_index

    left = 0 
    right = len(nums)

    while left < right:

      mid = (left + right) // 2

      # if we are not past the kth missing number
      if missing_numbers(mid) < k:
        left = mid + 1
      else:
        right = mid
    
    # return nums[left - 1] + k - missing_numbers(left - 1)
    # equivalent to 
    # nums[left - 1] + k - (nums[left - 1] - nums[0] - (left - 1))
    # k + nums[0] + left - 1
    # makes sense since there are two offsets
      # k is from the problem but we may not have all missing numbers immediately 
      # left tells us where we start to go beyond k missing numbers so we go back 1
    return nums[0] + k + (left - 1)

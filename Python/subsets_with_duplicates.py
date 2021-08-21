"""
BFS to generate the powerset
  however we need to avoid adding duplicates
  array is not sorted but when we sort when can check adjacent values for duplicates

we can keep track of the previous subsets where we added the previous element
  that way we can loop through that rather than all of the subsets so far
  this essentially cuts the loop in half
"""

def find_subsets(nums):
  # sort the array
  nums.sort()
  
  # add the empty subset
  subsets = []
  subsets.append([])
  
  # loop through each element in the given list
    # check if the previous element and the current elements are the same
      # start in the middle of the subsets so far
    # loop through the subsets
      # make a copy of the current subset in subsets
      # append the current element to the copy
      # append the copy to subsets
  
  for curr in range(len(nums)):
    # start with all of the current subsets
    start = 0
    
    # if we are not at the end and we have a duplicate then skip to the first index of the previous group of subsets
    if curr > 0 and nums[curr] == nums[curr - 1]:
      start = end + 1

    # duplicate up to the last subset of the previous addition
    end = len(subsets)
    for i in range(start, end):
      copy = list(subsets[i]) # apparently copy is not a list inside the list named subsets so we need list()
      copy.append(nums[curr])
      subsets.append(copy)

  return subsets

# O(N * 2^N) time complexity, where N is the length of the given array. For each element we add it to previously generated subsets. We double the number of subsets in the worst case which doubles the number of steps in the inner for loop.
# O(N * 2^N) space complexity since that is the size of our output array.

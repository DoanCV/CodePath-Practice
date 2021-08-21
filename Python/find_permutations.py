"""
[1,3,5]
place after, before, in between

                                [1]
                           /          \
                      [1,3]            [3,1]
                        /                \
        [1,3,5],[5,1,3],[1,3,5]     [3,1,5],[5,3,1],[3,5,1]

we can use BFS with a queue to keep track of the old permutations and then insert the current value in all positions of the old permutations
OR
we can use recursion
"""

def find_permutations(nums): 
  result = []
  index = 0
  curr_permutation = []
  recurse(nums, index, result, curr_permutation)
  return result

# helper function 
def recurse(nums, index, result, curr_permutation):
  # if we are finished building the permutation, add it to the result
  if index == len(nums):
    result.append(curr_permutation)

  # build the permutation
    # loop through the index of old permutations and insert the value at the current index in nums
      # create a copy 
      # insert at the index of old permutations
      # recurse to the value at the next position with the copy of the current permutation
  else:
    for i in range(len(curr_permutation) + 1):
      new_permutation = list(curr_permutation)
      new_permutation.insert(i, nums[index])
      recurse(nums, index + 1, result, new_permutation)

def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()

# O(N! * N) time complexity, where N is the length of the given array, since we know there are N! permutations and to create each of these permutations we insert into each index which takes O(N) time.
# O(N! * N) space complexity since that is the size of our output. There are N! permutations of length N.

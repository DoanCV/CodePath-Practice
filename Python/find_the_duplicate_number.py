"""
# we only have one number being duplicated but it can be duplicated multiple times
# we are guranteed a duplicate 

Cyclic sort:
while we are not at the end of the array

  if the current value is in the wrong position

    if the value at the position of the current value is not the same 
      we swap
    otherwise the two values we are swapping are the same then we found our duplicate

  else
    increment the current position

ex. 
nums = [1,4,4,3,2]

i = 0
nums[i] = 1
nums[ nums[i] - 1 ] = 1
same so increment i
nums = [1,4,4,3,2]

i = 1
nums[i] = 4
nums[ nums[i] - 1 ] = 3
not the same so swap
nums = [1,3,4,4,2]

i = 1
nums[i] = 3
nums[ nums[i] - 1 ] = 4
not the same so swap
nums = [1,4,3,4,2]

i = 1
nums[i] = 4
nums[ nums[i] - 1 ] = 4
they are the same numbers so that is our duplicate
"""

def find_duplicate(nums):
  i = 0
  while i < len(nums):
    
    if nums[i] - 1 != i:

      current = nums[i] - 1
      if nums[i] != nums[current]:
        nums[i], nums[current] = nums[current], nums[i]  # swap
      else:  # we have found the duplicate
        return nums[i]

    else:
      i += 1
  # no need to return anything at this point since we are guranteed a number will be duplicated
  
  
# O(N) time complexity, where N is the length of the given array, since in the worst case we complete everything in one loop with no repeated steps.
# O(1) space complexity since we are not using any extra data structures.

"""
Follow up:
Can you do this without modifiying the input array and still use O(1) space?
Joma Tech (Anime): Trivial

We can use tortoise and hare to find a cycle and then we find the start of this cycle. 
We have a cycle because of the Pigeonhole principle and the assumption that we have N + 1 numbers from 1 to N.
The start of the cycle is the duplicate number.

# find the cycle

# find the length of the cycle

# jump the fast pointer (now slow) back to the start of the array

# move both these pointers until they meet, this is the start of the cycle

ex. nums = [1,4,4,3,2]
slow = nums[0] = 1
"""

def find_duplicate(nums):

  # find cycle
  slow = nums[0]
  fast = nums[nums[0]]
  while slow != fast:
    slow = nums[slow]
    fast = nums[nums[fast]]
  
  # find length of cycle
    # create another pointer go to the next element after where slow left off in the cycle and keep going until we find the slow pointer again
  curr = nums[nums[slow]]
  cycle_length = 1
  while start != nums[slow]:
    curr = nums[curr]
    cycle_length += 1
  
  return cycle_start(nums, cycle_length)

def cycle_start(nums, cycle_length):
  # move one pointer to cycle_length
  ptr1 = nums[0]
  ptr2 = nums[0]
  while cycle_length > 0:
    ptr2 = nums[ptr2]
    cycle_length -= 1

  # move both pointers one at a time until they meet
  while ptr1 != ptr2:
    ptr1 = nums[ptr1]
    ptr2 = nums[ptr2]

  # return the value that they are the same, this is the start of the cycle
  return ptr1

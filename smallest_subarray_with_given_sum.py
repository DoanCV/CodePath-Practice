def smallest_subarray_with_given_sum(s, arr):
  """ sliding window
  keep track of:
  window_start = 0
  window_end
  curr_sub_array = [] 
    necessary for length check
  curr_sub_array_sum = 0
  min_length 
    return variable 
    the window size is not set
    return 0 if none exists

  loop through the length of array with window_end
    keep adding arr[window_end] to curr_sub_array_sum until...

    while the curr_sum is greater than or equal to target value
      compare the length
      if the length (end - start + 1) is shorter than (anything bigger than the original)
        save the length
        if min_length == 1
          return 1
      substract start index value out from the curr_sub_array_sum
      add one to the window start index

  if the length is not less than or equal to original (can just be anything greater then length)
    return min_length
  else
    return 0


  [1,2,3,4,5], s = 4
  [1] too small
  [1,2] too small
  [1,2,3] works min_length = 3
  # usually [2,3,4] is next but we need to check for [2,3] first, obviously adding more on something that works will still work and is useless
  # shrink
  [2,3] works min_length = 2
  # keep shrinking
  [3] too small
  [3,4] works min_length = 2
  # keep shrinking
  [4] works min_length = 1
  To make it a bit faster, if I see min_length = 1, I will just stop, I'm looking for first instance, the minimum possible length is 1
  [4,5] works min_length = 2
  # keep shrinking
  [5] works min_length = 1

  ans = 1
  """

  window_start = 0
  curr_sub_array_sum = 0 
  min_length = len(arr) + 1

  for window_end in range( len(arr) ):
    curr_sub_array_sum += arr[window_end]

    while( curr_sub_array_sum >= s ): 
      if window_end - window_start + 1 < min_length:
        min_length = window_end - window_start + 1
        if min_length == 1:
          return 1
      curr_sub_array_sum -= arr[window_start]
      window_start += 1

  if min_length < len(arr) + 1:
    return min_length
  else:
    return 0
  return -1

# O(N + N) time complexity since the outer for loop traverses the full length of the array and the innder while loop follows along but there is no recomputation. 
  # The for loop moves the window_end
  # The while loop moves the window_start
  
# O(1) space complexity since even though the window size is variable, it is bounded by the length of the given array which is constant.

def max_sub_array_of_size_k(k, arr):
  """ sliding window
  variables:
  window start
  window end
    keep the length of the window equal to k
  keep track of max sum
  keep track of indicies of max sum

  logic:
  loop over window end
    keep adding contiguous values
    calculate sum
    compare to max sum, if greater update and store indicies that contribute to this max sum
      subtract value at window start
      make the next index the new window start

  how many times to loop:
    ex.
      [1,2,3,4,5,6,7], k = 3
      [1,2,3] = 6
      [2,3,4] = 9
      [3,4,5] = 12
      [4,5,6] = 15
      [5,6,7] = 18
      length of array = 7
      k = 3
      loop through 5 times = length of array - k + 1

     small ex. to walk through code
      [1,2,3,4,5], k = 3
      [1,2,3] = 6
      [2,3,4] = 9
      [3,4,5] = 12
      length of array = 5
      k = 3
      loop through 3 times = length of array - k + 1  
  """

  # The commented out code is for follow up question:
  #   can you return that subarray?

  window_start = 0
  max_sum = 0
  curr_sum = 0
  # curr_result = []

  for window_end in range( len(arr) ):
    curr_sum += arr[window_end]
    # curr_result.append(window_end)
    
    if window_end >= k - 1:
      # I will only report the first instance of the max sum
      if curr_sum > max_sum:
        max_sum = curr_sum
        # result = curr_result

      # curr_result.pop(0)
      curr_sum = curr_sum - arr[window_start]
      window_start += 1 
  return max_sum

  return -1
  
# O(N) time complexity, where N is the size of array arr since I loop through the array once and I do not recompute sums with overlapping windows
# O(1) space complexity, since the size of the window that I calculate on is constant.

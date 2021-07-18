def length_of_longest_substring(arr, k):
  """ sliding window since contiguous subarray
  questions:
    empty array? nah
    detect 0s and 1s? nah, all valid inputs
  
  keep track of:
  window_start = 0
  window_end
  int_count = {}
  max_length = 0
    return value
    we are trying to maximize this
    equal to window size 
  
  logic:
  loop over the length of the array with window_end
    if number at position window_end is not in int_count
      the frequency of the number at position window_end is 0
    increment the frequency of the number at window_end by 1

    while the count of 0s is more than k
      # shrink

    if the window size is greater than the max_length
      update max_length 
  
  reutrn max_length
  
  ex. 
  [1,0,0,1,1,0], k = 2
  [1] valid, max = 1
  [1, 0] valid, max = 2
  [1, 0, 0] valid, max = 3
  [1, 0, 0, 1] valid, max = 4
  [1, 0, 0, 1, 1] valid, max = 5
  [1, 0, 0, 1, 1, 0] invalid
    [0,0,1,1,0]
    [0,1,1,0] valid, max = 5
  """
  window_start = 0
  max_length = 0
  int_count = {}

  for window_end in range(len(arr)):
    end_int = arr[window_end]
    if end_int not in int_count:
      int_count[end_int] = 0
    int_count[end_int] += 1

    while int_count[0] > k:
      start_int = arr[window_start]
      int_count[start_int] -= 1
      window_start += 1
    
    if window_end - window_start + 1 > max_length:
      max_length = window_end - window_start + 1 
  
  return max_length

  return -1

# O(N) time complexity, where N is the length of the given array, since we are using sliding window and not recomputing values while traversing the array once.
# O(1) space complexity, which is simplified from O(2) since 2 is the size of the hash table. The only 2 possible valid inputs.

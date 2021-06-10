def pair_with_targetsum(arr, target_sum):
  """ two pointer since the array is already sorted
  keep track of:
  start = 0
  end = len(arr) - 1
  
  we are trying to return the indicies of the pair, not the actual value of the pairs

  logic:
  while start < end:
    if arr[start] + arr[end] == target_sum:
      return [start, end]
    elif arr[start] + arr[end] > target_sum:
      end -= 1
    elif arr[start] + arr[end] < target_sum:
      start += 1
  return None

  """
  start = 0
  end = len(arr) - 1
  while start < end:
    if arr[start] + arr[end] == target_sum:
      return [start, end]
    elif arr[start] + arr[end] > target_sum:
      end -= 1
    elif arr[start] + arr[end] < target_sum:
      start += 1

  return None
  return [-1, -1]

# O(N) time complexity, where N is the length of the given array, since the worst case the two pointers meet in the middle, having traveled N/2 positions each. O(N/2) is asymotaotically O(N).
# O(1) space complexity since we are not creating any data structures.

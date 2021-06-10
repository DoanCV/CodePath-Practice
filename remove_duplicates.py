def remove_duplicates(arr):
  """ two pointer since the array is sorted
  keep track of:
  curr = 1
  non_duplicate = 1
  current array, not variable but a concept
    we want to solve in place and assuming we are allowed to change the input, i will change value at non_duplicate since array is mutable
  max_length
    return value
    we are trying to maximize this 
    
  
  logic:
  while curr < len(arr):
    if arr[curr - 1] != arr[curr]:
      arr[non_duplicate] = arr[curr]
      non_duplicate += 1
    curr += 1
  return non_duplicate

  ex. 
  [2,2,2,11] 
  [2] curr = 1, non_duplicate = 1
  [2,2] curr = 2, non_duplicate = 1
  [2,2,2] curr = 3, non_duplicate = 1
  [2,2,2,11] curr = 4, non_duplicate = 1
    # swap
    [2,11,2,2] curr = 4, non_duplicate = 2
  max_length = 2

  ex. 
  [2,2,2,11,11,11] 
  [2] curr = 1, non_duplicate = 1
  [2,2] curr = 2, non_duplicate = 1
  [2,2,2] curr = 3, non_duplicate = 1
  [2,2,2,11] curr = 4, non_duplicate = 1
    [2,11,2,2] 
  [2,11,2,2,11] curr = 5, non_duplicate = 2
  [2,11,2,2,11,11] curr = 6, non_duplicate = 2
  max_length = 2
  """
  curr = 1
  non_duplicate = 1
  while curr < len(arr):
    if arr[curr - 1] != arr[curr]:
      arr[non_duplicate] = arr[curr]
      non_duplicate += 1
    curr += 1
  return non_duplicate

  return -1

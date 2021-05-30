def longest_substring_with_k_distinct(str, k):
  """ sliding window (since substrings are not reorderable)
  keep track of:
  the unique character count
    hash table
      char: count
  length of the substring
    return value
    we are trying to maximize this
  window_start = 0
  window_end
  
  logic:
  loop through length of string with the window_end
    append character to hash table
      if character is already in hash table, count += 1
      else count = 1
    
    loop through all keys of the hash table
      if the unique character (value of hash table) count is greater than k
      shrink the current window
        window_start += 1
  
  """
  return -1

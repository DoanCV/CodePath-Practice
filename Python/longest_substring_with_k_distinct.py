def longest_substring_with_k_distinct(str_given, k):
  """ sliding window (since substrings are not reorderable)
  keep track of:
  the unique character count
    hash table
      char: count
  max length of the substring
    return value
    we are trying to maximize this
  window_start = 0
  window_end
  window size
  
  logic:
  loop through length of string with the window_end
    append character to hash table
      if character is not already in hash table, count = 0
    count += 1
    
    while the unique character (value of hash table) count is greater than k
      shrink the current window
        subtract 1 from the frequency of the first character in substring since that is part of shrinking
        window_start += 1
    
    check if there is a new max, save if true
  
  """
  window_start = 0
  max_length = 0
  char_counts = {}

  for window_end in range( len(str_given) ):
    end_char = str_given[window_end] 
    if end_char not in char_counts:
      char_counts[end_char] = 0
    char_counts[end_char] += 1

    while len(char_counts) > k:
      start_char = str_given[window_start]
      char_counts[start_char] -= 1
      # when the count hits zero delete the character b/c it contributes to length 
      if char_counts[start_char] == 0:
        del char_counts[start_char]
      window_start += 1

    if window_end - window_start + 1 > max_length:
      max_length = window_end - window_start + 1

  return max_length

  return -1

# O(N + N) time complexity, where N is the length of the string, since we traverse through the length of the string once with a sliding window. Values are not reinserted or recalculated.
  # ⁂ O(N) as O(N + N) asymptotically is just O(N)

# O(K) space complexity, where k is the size of the window which is the size of the hash table we are inserting into.

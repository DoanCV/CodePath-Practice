def non_repeat_substring(str_given):
  """ sliding window bc of substring
  keep track of:
  window_start = 0
  window_end
  max_length = 0
    return value
    we are trying to maximize this
    size of window
    end - start + 1
  char_count = {}
    length of hash table is the number of characters
    value at each key must be 1, i dont care about length
    i will keep substracting 1 from count while shrinking to keep valid substring

  logic:
  loop through the length of the array with window_end
    if the current character at index window_end is not in char_count
      the count at key of current char is 0
    increment count of current char by 1

    while current_char[current char] > 1:
      # shrink until == 1
      subtract 1 from the count of window_start char
      increment window_start by 1

    # check if the window size is greater than max_length, if so save
  
  # return max_length

  ex:
    "aabccbb"
    {a:1} valid. max = 1
    {a:2} invalid, must shrink. 
      "aa" remove first 'a' from window
      {a:1} max = 1
    {a:1, b:1} valid. max = 2
    {a:1, b:1, c:1} valid. max = 3 
    {a:1, b:1, c:2} invalid, must shrink.
      "abcc" remove 'abc' from the window
      {a:0, b:0, c:1} max = 3
    {a:0, b:1, c:1} valid. max = 3
    {a:0, b:2, c:1} invalid, must shrink.
      "cbb" remove 'cb' from window
      {a:0, b:1, c:0} max = 3
    ans = 3
  """

  window_start = 0
  max_length = 0
  char_count = {}

  for window_end in range(len(str_given)):
    end_char = str_given[window_end]
    if end_char not in char_count:
      char_count[end_char] = 0
    char_count[end_char] += 1

    while char_count[end_char] > 1:
      start_char = str_given[window_start]
      char_count[start_char] -= 1
      window_start += 1
    
    if window_end - window_start + 1 > max_length:
      max_length = window_end - window_start + 1

  return max_length

  return -1

# O(N) where N is the length of the string. I traverse through the string once and do not recompute. 
# O(k) where k is the length of the hashtable. Since we know the string only has alphabet k is at most 26. k is also at most n since they are only equal when the entire string has no repeating characters. If there were repeating characters, the hashtable length would be smaller.

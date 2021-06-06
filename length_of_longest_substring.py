def length_of_longest_substring(str_given, k):
  """sliding window bc of maximum length substring
  keep track of:
  window_start = 0
  window_end
  char_count = {}
  max_length = 0
  max_repeat_count = 0
    use this to check if we need to shrink
    only one char can be as high as it wants but the count of all other characters must be at most k since we can only replace at most k

  logic:
  loop through the length of the string with window_end
    if the char at postiion window_end is not in char_count
      value at key char at position window_end is 0
    increment value at key char at position window_end by 1

    if the value at key char at position window_end is greater than max_repeat_count 
      the new max_repeat_count is the value at key char at position window_end

    while the window size - max_repeat_count > k:
      #shrink
      get the start_char, subtract 1 from count
      increment window_start by 1
    
    # check if window size is greater than max length, if so update
  
  return max_length
  """
  window_start = 0
  max_length = 0
  max_repeat_count = 0
  char_count = {}

  for window_end in range( len(str_given) ):
    end_char = str_given[window_end]
    if end_char not in char_count:
      char_count[end_char] = 0
    char_count[end_char] += 1

    if char_count[end_char] > max_repeat_count:
      max_repeat_count = char_count[end_char]
    
    while ( ( window_end - window_start + 1 ) - max_repeat_count > k ):
      start_char = str_given[window_start]
      char_count[start_char] -= 1
      window_start += 1

    if window_end - window_start + 1 > max_length:
      max_length = window_end - window_start + 1
  
  return max_length

  return -1

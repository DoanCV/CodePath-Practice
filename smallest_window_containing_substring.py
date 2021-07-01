"""
sliding window becuase of substring

keep track of:
minimum_length
  to check if the current substring is smaller than the smallest so far
  initialize as inf or one greater than the length of the given string
window_start
window_end
counts
  hashmap (letter: frequency)
smallest_substring
  return value
  string

logic:
loop through the string
  keep track of the frequency of each character

loop through the length of the string with window_end
  if character at position window_end in counts decrement
    if there is a match increment count
  
  shrink the window and stop when a match is removed
    update length if possible and if there is a new answer then save the start of this substring


if there is no answer return empty string

return the substring (start of substring to start of substring plus minimum length)
"""

def find_substring(str_given, pattern):
  window_start = 0
  minimum_length = len(str_given) + 1
  matches = 0
  start_of_substring = 0
  counts = {}

  for i in pattern:
    if i not in counts:
      counts[i] = 0
    counts[i] += 1
  
  for window_end in range(len(str_given)):
    right_char = str_given[window_end]
    if right_char in counts:
      counts[right_char] -= 1
      # we dont care since we just need the characters in the pattern, duplicates are fine
      if counts[right_char] >= 0:
        matches += 1

    while matches == len(pattern):
      if window_end - window_start + 1 < minimum_length:
        minimum_length = window_end - window_start + 1
        start_of_substring = window_start
      
      left_char = str_given[window_start]
      if left_char in counts:
        if counts[left_char] == 0:
          matches -= 1
        counts[left_char] += 1
      window_start += 1
    
  if minimum_length > len(str_given):
    return ""

  return str_given[start_of_substring : start_of_substring + minimum_length]

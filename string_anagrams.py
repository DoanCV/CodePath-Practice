""" sliding window of size length of given pattern
keep track of:
window_start
window_end
counts
  hashmap with the frequency of characters
freq_matches
  matches based on frequency, if we account for the frequency of each distinct character then we can modify matches


logic:
# basically permutation of string but we are saving the value of window_start in result_indexes
loop through given pattern, store frequency in counts

loop through the length of the given string with window_end
  decrement frequency of character at position window_end in counts if in counts
  if frequency of character at position window_end is 0 increment freq_matches by 1

  if freq_matches == len(counts):
    append window_start to result_indexes
  
  while window_end >= len(given string) - 1
    # shrink
    if character at position window_start is in counts
      if the frequency of the character at position window_start is 0
        decrement freq_matches by 1
      increment the frequency of the character at position window_start
    increment window_start by 1

return result_indexes
"""

def find_string_anagrams(string, pattern):
  result_indexes = []
  window_start = 0
  freq_matches = 0
  counts = {}

  for i in pattern:
    if i not in counts:
      counts[i] = 0
    counts[i] += 1
  
  for window_end in range(len(string)):
    right_char = string[window_end]
    if right_char in counts:
      counts[right_char] -= 1
      if counts[right_char] == 0:
        freq_matches += 1
    
    if freq_matches == len(counts):
      result_indexes.append(window_start)
    
    if window_end >= len(pattern) - 1:
      left_char = string[window_start]
      if left_char in counts:
        if counts[left_char] == 0:
          freq_matches -= 1
        counts[left_char] += 1
      window_start += 1  

  return result_indexes


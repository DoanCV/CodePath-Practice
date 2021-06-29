""" sliding window
keep track of:
hashmap for the character frequency
size of the window
  length of the given pattern
window_start
window_end
freq_matches
  matches based on frequency
  if freq_matches is equal to the length of the hashmap then there is a permutation of the pattern in the given string
    that is, if the count of each distinct character has been accounted for freq_matches amount of times then we have a perfect match

logic:
# as long as the size of the window is the length of the pattern we can just keep track of the frequencies

loop through the length of the pattern and keep track of the character count 
loop through the length of the given string with window_end
  # add character at position window_end to window
  if character at position window_end is in hashmap
    subtract frequency from hashmap
    if frequency of char at position window_end is 0
      increment freq_matches by 1 since we have a match of frequency
  
  if the length of the hashmap is equal to freq_matches
    return True
  
  if the length of the hashmap is greater than that of the length of the pattern
    # shrink

    if the character at window_start is in the hashmap
      decrement the matches if the frequency of the character at window_start is 0
      increment the frequency of the character at window_start by 1
    
    increment window_start by 1

return False
"""

def find_permutation(string, pattern):
  counts = {}
  window_start = 0
  freq_matches = 0

  for char in range(len(pattern)):
    if pattern[char] not in counts:
      counts[pattern[char]] = 0
    counts[pattern[char]] += 1

  for window_end in range(len(string)):
    right_char = string[window_end]
    if right_char in counts:
      counts[right_char] -= 1
      if counts[right_char] == 0:
        freq_matches += 1
    
    if freq_matches == len(counts):
      return True
    
    if window_end >= len(pattern) - 1:
      left_char = string[window_start]
      if left_char in counts:
        if counts[left_char] == 0:
          freq_matches -= 1
        counts[left_char] += 1
      window_start += 1

  return False

# O(N + M) time complexity, where N is the length of the given string and M is the length of the given pattern, since we have to pass through the length of each string once
# O(M) space complexity since worst case the pattern has only distinct characters so the length of the hashtable is equal to the length of the given pattern.

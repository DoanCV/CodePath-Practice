from heapq import *

def sort_character_by_frequency(str):
  """
  strings are immutable so we need to create another string to return the results

  get frequencies in hashmap (char: frequency)
  add to heap
    we are using a heap but storing the negation of frequencies
    that way when we pop we the the higher frequencies first to add to the result string
  """
  freq = {}
  for i in str:
    if i not in freq:
      freq[i] = 0
    freq[i] += 1
  
  heap = []
  for key, value in freq.items():
    heappush(heap, (-value, key))

  result = ""
  while len(heap) > 0:
    value, key = heappop(heap)
    curr = key * (-value)
    result += curr

  return result

# O(NlogN + N) time complexity.
# O(N) space complexity.

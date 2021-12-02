"""
just by looking at the examples we can figure out what comes before what since everything is ordered. we can think of each letter as a node and the ordering directs one node to another. there cannot be cycles since there will be a tie and that is not a valid ordering

use topological sort to get a valid ordering
  build graph with adjacency list

"""
from collections import deque
def alienOrder(words):

  adjecency_list = {}
  for word in words:
    for char in word:
      if char not in adjecency_list:
        adjecency_list[char] = set()

  indegrees = {i: 0 for i in range(26)}

  for i in range(1, len(words)):
    first_word = words[i-1]
    second_word = words[i]

    length = min(len(first_word), len(second_word)) # we cant guarantee same length words

    for j in range(length):
      # scan two words at a time to see the difference, that is how we will know what a letter depends on 

      if first_word[j] != second_word[j]:
        charOut = first_word[j]
        charIn = second_word[j]

        # if this is the first time we found the edge
        if charIn not in adjecency_list[charOut]:
          adjecency_list[charOut].add(charIn)
          indegrees[ord(charIn) - ord("a")] += 1 # increase indegree

        break
      
      # edge case 
      # if we have a longer first word like "zay" that has the same prefix as the seocnd word like "za" we will miss it and can get the wrong answer since the first cant come before the second in this case
      # take advantage of the for else, when we never break like in the "if" of the case above then we go to the else
      else:
        if len(first_word) > len(second_word):
          return ""
  
  # BFS
  ordering = ""
  queue = deque([node for node in adjecency_list if indegrees[ord(node) - ord("a")] == 0]) # add all sources ie indegree of 0

  while queue:
    curr_char = queue.popleft()
    ordering = ordering + curr_char

    for neighbor_char in adjecency_list[curr_char]:
      indegrees[ord(neighbor_char) - ord("a")] -= 1
      
      # if it is now a source add to queue
      if indegrees[ord(neighbor_char) - ord("a")] == 0:
        queue.append(neighbor_char)

  # if we have DAG we return ordering else no valid dictionary
  if len(ordering) == len(adjecency_list):
    return ordering
  else:
    return ""
